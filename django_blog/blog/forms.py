from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment


# ==========================
# USER REGISTRATION FORM
# ==========================

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ==========================
# POST FORM 
# ==========================

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


# ==========================
# COMMENT FORM
# ==========================

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
