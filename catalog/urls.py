from django.urls import path

from catalog.views import index, contact_info

urlpatterns = [
    path('', index, name='index'),
    path('contact_info/', contact_info, name='contact_info'),
]
