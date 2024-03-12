from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView

from blog.models import Blog


# CBV на отображение главной страницы приложения
class BlogView(TemplateView):
    template_name = 'blog/blog.html'
    extra_context = {
        'title': 'Блог'
    }

    # Загрузка контента на страницу
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Blog.objects.all()
        return context_data


# CBV на загрузку опубликованного контента
class BlogPublishedView(TemplateView):
    template_name = 'blog/blog_published.html'
    extra_context = {
        'title': 'Блог'
    }

    # Загрузка контента на страницу
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Blog.objects.all()
        return context_data


# CBV на создание нового блога
class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'content', 'preview')
    success_url = reverse_lazy('blog:blog')


# CBV на изменение существующего блога
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'preview')

    def get_success_url(self):
        # Получаем объект, который был отредактирован
        edited_object = self.object
        # Получаем URL-адрес страницы просмотра объекта, который был отредактирован
        return reverse('blog:blog_view', args=[edited_object.slug])


# CBV на удаление блога
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')


# CBV на просмотр выбранного блога
class BlogDetailView(DetailView):
    model = Blog

    def get(self, request, *args, **kwargs):
        # Получаем объект блога
        blog = self.get_object()
        # Увеличиваем счетчик просмотров на 1
        blog.count_views += 1
        blog.save()
        return super().get(request, *args, **kwargs)

    # фильтрация объектов по указанному slug адресу
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(slug=self.kwargs.get('slug'))
        return queryset

    # загрузка контента на страницу
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Название блога: "{self.object.name}"'
        context['category_pk'] = self.object.pk
        return context


# Контролер на публикацию/де-публикацию блога
def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.published:
        blog_item.published = False
    else:
        blog_item.published = True

    blog_item.save()

    return redirect(reverse('blog:blog'))
