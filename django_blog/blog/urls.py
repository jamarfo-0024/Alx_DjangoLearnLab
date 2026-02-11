from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Register
    path('register/', views.register, name='register'),

    # Profile
    path('profile/', views.profile, name='profile'),
]
