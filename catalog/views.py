from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from catalog.models import Category, Product


# Стартовая страница приложения Catalog
class IndexView(TemplateView):
    template_name = 'catalog/start_form.html'
    extra_context = {
        'title': 'Склад товаров',
        'view': 'Просмотр товаров'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()
        return context_data


# Страница с контактными данными
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'name: {name}, email: {email}, message: {message}')
    return render(request, 'catalog/contacts.html')


# Страница с продуктами по выбранным категориям
class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = 'Склад товаров',
        context_data['view'] = 'Купить товар'

        return context_data
