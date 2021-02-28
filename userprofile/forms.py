from django import forms
from userprofile.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','caption',]