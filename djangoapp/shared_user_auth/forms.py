from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input is-primary', 'placeholder': 'petersagan', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input is-primary', 'placeholder': '*********', 'id': 'password'}))


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'input is-primary',
                'placeholder': 'petersagan',
                'id': 'username'
            }))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'input is-primary',
                'id': 'password',
                'placeholder': '******'
            }),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'input is-primary',
                'id': 'confirm-password',
                'placeholder': '******'
            }),
    )
