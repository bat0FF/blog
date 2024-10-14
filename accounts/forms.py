from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={"class": "form-control mb-1", 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control mb-1"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Ваше имя'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Ваша фамилия'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите e-mail'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={"class": "form-control mb-1", 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(max_length=50,
                               required=True, label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control mb-1", 'placeholder': 'Пароль'}))
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
