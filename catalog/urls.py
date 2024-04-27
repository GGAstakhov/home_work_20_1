from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, IndexView, ProductListView, ProductCreateView, ProductUpdateView, CategoryCreateView, ProductDeleteView, ProductDetailView

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
    # Просмотр товара
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
]
