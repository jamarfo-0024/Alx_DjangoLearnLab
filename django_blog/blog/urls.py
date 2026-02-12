from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    # Authentication
    register,
    profile,

    # Post CRUD
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,

    # Comment CRUD 
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [

    # =========================
    # AUTHENTICATION URLS
    # =========================

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('register/', register, name='register'),

    path('profile/', profile, name='profile'),


    # =========================
    # POST CRUD URLS
    # =========================

    path('post/', PostListView.as_view(), name='post-list'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    # =========================
    # COMMENT CRUD URLS
    # =========================

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),

    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
