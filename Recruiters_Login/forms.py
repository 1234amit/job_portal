from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Recruiters_Login.models import Recruiters


class CreateNewRecruiter(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))

    class Meta:
        model = User
        fields = ('email', 'username','password1','password2')

class EditProfile(forms.ModelForm):
    class Meta:
        model = Recruiters
        exclude = ('user',)
