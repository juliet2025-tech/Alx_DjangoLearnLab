from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        # blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags
        widgets = {
            'tags': TagWidget(),  # nice input for multiple tags
        }