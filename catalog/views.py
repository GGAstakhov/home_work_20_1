# Импорт необходимых модулей
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from catalog.forms import ProductForm, CategoryForm, ProductVersionForm
from django.urls import reverse_lazy
from django.shortcuts import reverse
from django import forms
from catalog.models import Product, Version, Category
from django.db.models import Case, When, CharField


# Стартовая страница приложения Catalog
class IndexView(TemplateView):
    template_name = 'catalog/start_form.html'
    extra_context = {
        'title': 'Склад товаров',
        'view': 'Просмотр товаров'
    }

    def get_context_data(self, **kwargs):
        # Получение данных контекста
        context_data = super().get_context_data(**kwargs)
        # Получение списка всех категорий
        context_data['object_list'] = Category.objects.all()
        return context_data


# Страница с контактными данными
class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        # Получение данных из запроса
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'name: {name}, email: {email}, message: {message}')
        return render(request, 'catalog/contacts.html')


# Страница с продуктами по выбранным категориям
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Получение всех продуктов по выбранной категории
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'))
        active_version = Version.objects.filter(is_active=True)
        return queryset.prefetch_related('version_set').annotate(active_version=Case(
            When(version__is_active=True, then='version__name'),
            default=None,
            output_field=CharField()
        ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_moderator'] = self.request.user.groups.filter(name='Модератор').exists()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'

    def get_context_data(self, **kwargs):
        # Получение данных контекста
        context = super().get_context_data(**kwargs)
        context['version_form'] = ProductVersionForm(prefix='version')
        return context

    def form_valid(self, form):
        # Проверка валидности формы
        self.object = form.save(commit=False)
        if self.request.user.is_authenticated:
            self.object.owner = self.request.user
        self.object.save()
        product = form.save(commit=False)
        product.name = form.cleaned_data['name']
        product.save()
        version_form = ProductVersionForm(self.request.POST, prefix='version')
        if version_form.is_valid():
            version = version_form.save(commit=False)
            version.product = product
            version.save()
        return redirect(reverse('catalog:product_list', kwargs={'pk': form.cleaned_data['category'].pk}))

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.groups.filter(name='Модератор').exists():
            # Скрыть поле публикации, если ты не модератор
            form.fields['is_published'].widget = forms.HiddenInput()
        return form


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модератор').exists()

    def get_success_url(self):
        product = self.get_object()
        return reverse('catalog:product_list', kwargs={'pk': product.category.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.groups.filter(name='Модератор').exists():
            # Скрыть поле публикации, если ты не модератор
            form.fields['is_published'].widget = forms.HiddenInput()
        return form


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'

    def get_success_url(self):
        product = self.get_object()
        return reverse('catalog:product_list', kwargs={'pk': product.category.pk})

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модератор').exists()


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create_category.html'

    def form_valid(self, form):
        # Проверка валидности формы
        self.object = form.save()
        return redirect(reverse('catalog:product_list', kwargs={'pk': self.object.pk}))


# Страница для редактирования продукта
class ProductDetailView(TemplateView):
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        # Получение данных контекста
        context_data = super().get_context_data(**kwargs)
        context_data['product'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context_data
