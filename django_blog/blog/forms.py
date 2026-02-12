from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment, Tag


# ==========================
# USER REGISTRATION FORM
# ==========================

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ==========================
# POST FORM (WITH TAG SUPPORT)
# ==========================

class PostForm(forms.ModelForm):

    # Comma separated tags input
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        # Handle tags
        tag_names = self.cleaned_data.get('tags', '').split(',')

        for name in tag_names:
            if name.strip():
                tag, created = Tag.objects.get_or_create(name=name.strip())
                instance.tags.add(tag)

        return instance


# ==========================
# COMMENT FORM
# ==========================

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
