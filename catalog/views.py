from django.shortcuts import render

from catalog.models import Category, Product


def start_form(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Склад товаров',
        'view': 'Просмотр товаров',
    }
    return render(request, 'catalog/start_form.html', context)


# Страница с контактными данными
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'name: {name}, email: {email}, message: {message}')
    return render(request, 'catalog/contacts.html')


# Страница с продуктами по выбранным категориям
def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': 'Склад товаров',
        'view': 'Купить товар',
    }
    return render(request, 'catalog/products.html', context)
