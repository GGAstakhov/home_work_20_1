from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, ProfileView, verify_email, reset_password
from users.apps import UsersConfig

# Установка имени приложения
app_name = UsersConfig.name

# Определение URL-шаблонов
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),  # URL для входа в систему
    path('logout/', LogoutView.as_view(), name='logout'),  # URL для выхода из системы
    path('register/', RegisterView.as_view(), name='register'),  # URL для регистрации
    path('profile/', ProfileView.as_view(), name='profile'),  # URL для профиля пользователя
    path('verify-email/', verify_email, name='verify_email'),  # URL для подтверждения почты пользователя
    path('reset-password/', reset_password, name='reset_password'),
]