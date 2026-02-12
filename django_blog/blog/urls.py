from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
    profile
)

from django.contrib.auth import views as auth_views
from .views import add_comment, update_comment, delete_comment



urlpatterns = [

    # -------------------------
    # Authentication URLs
    # -------------------------

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('register/', register, name='register'),

    path('profile/', profile, name='profile'),


    # -------------------------
    # Blog CRUD URLs 
    # -------------------------

    path('post/', PostListView.as_view(), name='post-list'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/comments/new/', add_comment, name='comment-add'),

    path('comment/<int:pk>/update/', update_comment, name='comment-update'),

    path('comment/<int:pk>/delete/', delete_comment, name='comment-delete'),

]

