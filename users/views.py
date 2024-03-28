from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from src.functions import send_mail, generate_password
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Класс для регистрации пользователя
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify_email')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data['email']
        # получаем код верификации из базы данных пользователя
        verification_code = f"Ваш код верификации: {User.objects.get(email=email).verification_code}"
        send_mail(email, 'Код подтверждения', verification_code)
        return response


# Класс для обновления профиля пользователя
class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    # Получение объекта пользователя
    def get_object(self, queryset=None):
        return self.request.user


# функция для вывода страницы с одним полем для подтверждения верификации пользователя
def verify_email(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        try:
            user = User.objects.get(verification_code=verification_code)
            if user.verification_code == verification_code:
                user.is_active = True
                user.is_verified = True
                user.save()
                return redirect('catalog:start_form')
        except User.DoesNotExist:
            messages.error(request, 'Неверный код верификации')
    return render(request, 'users/verify_email.html')


# Функция для восстановления пароля пользователя
def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = generate_password(length=10)
            # перезаписываем пароль пользователя
            user.set_password(new_password)
            user.save()
            new_password_text = f'Ваш новый пароль:\n{new_password}'
            # отправляем письмо с новым паролем пользователя
            send_mail(email, 'Восстановление пароля', new_password_text)
            return redirect('users:login')
        except User.DoesNotExist:
            messages.error(request, 'Неверный email')
    return render(request, 'users/recover_password.html')