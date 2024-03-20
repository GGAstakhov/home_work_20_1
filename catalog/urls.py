from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, IndexView, ProductsListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryCreateView

# Конфигурационное имя приложения
app_name = CatalogConfig.name

# Ссылки на страницы приложения Catalog
urlpatterns = [
    path('', IndexView.as_view(), name='start_form'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', ProductsListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
]
