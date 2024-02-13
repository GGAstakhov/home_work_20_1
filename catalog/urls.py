from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import start_form, contacts, products

# Конфигурационное имя приложения
app_name = CatalogConfig.name

# Ссылки на страницы приложения Catalog
urlpatterns = [
    path('', start_form, name='start_form'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>products/', products, name='products'),
]
