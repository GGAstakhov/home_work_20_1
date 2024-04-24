from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, IndexView, ProductListView, ProductCreateView, ProductUpdateView, CategoryCreateView, ProductDeleteView

# Конфигурационное имя приложения
app_name = CatalogConfig.name

# Ссылки на страницы приложения Catalog
urlpatterns = [
    path('', IndexView.as_view(), name='start_form'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
]
