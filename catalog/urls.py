from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, IndexView, ProductsListView

# Конфигурационное имя приложения
app_name = CatalogConfig.name

# Ссылки на страницы приложения Catalog
urlpatterns = [
    path('', IndexView.as_view(), name='start_form'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', ProductsListView.as_view(), name='products'),
]
