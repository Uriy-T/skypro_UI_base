import os
from dotenv import load_dotenv
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from .forms import CreateUser, LoginForm, UpdateUser
from .models import CustomBaseUser

load_dotenv()

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CreateUser
    success_url = reverse_lazy('catalog:category_list')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = os.getenv('MAIL_FROM')
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

class UpdateUserView(UpdateView):
    model = CustomBaseUser
    form_class = UpdateUser
    template_name = 'users/user_update.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('catalog:category_list')

class LogInView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('catalog:category_list')

class LogOutView(LogoutView):
    pass