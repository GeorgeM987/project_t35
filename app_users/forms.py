from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=50, required=False)

    class Meta():
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone = self.cleaned_data.get('phone')
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    class Meta():
        model = User
        fields = ['username', 'password']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Name: ', required=True)
    email = forms.EmailField(label='Email: ', required=True)

    class Meta():
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(max_length=50, label='Phone: ', required=False)
    image = forms.ImageField(label='Image: ', required=True)

    class Meta():
        model = Profile
        fields = ['phone', 'image']