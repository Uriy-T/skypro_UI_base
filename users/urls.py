
from django.urls import path
from .views import RegisterView, UpdateUserView, LogInView, LogOutView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user_update/', UpdateUserView.as_view(), name='update_profile'),
    path('login/', LogInView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogOutView.as_view(next_page='catalog:category_list'), name='logout'),
]
