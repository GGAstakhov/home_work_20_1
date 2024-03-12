from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView, BlogCreateView, BlogUpdateView, BlogDeleteView, toggle_activity, \
    BlogPublishedView, BlogDetailView

app_name = BlogConfig.name

# url адресация в приложении Blog
urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('published/', BlogPublishedView.as_view(), name='blog_published'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('<str:slug>/', BlogDetailView.as_view(), name='blog_view'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
