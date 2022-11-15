from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [
    path('', profile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(
        template_name='customer/login.html'), name='user-login'),
    path('logout/', auth_views.LoginView.as_view(
        template_name='customer/logout.html'), name='user-logout'),
    path('register/', register, name='user-register'),
    path('profile/update/', profile_update,
         name='user-profile-update'),
]





