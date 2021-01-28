from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input is-primary',
            'placeholder': 'petersagan',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input is-primary',
            'placeholder': '********',
        })


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
          'class': 'input is-primary',
          'placeholder': 'petersagan',
        })
        self.fields['password1'].widget.attrs.update({
          'class': 'input is-primary',
          'placeholder': '********',
        })
        self.fields['password2'].widget.attrs.update({
          'class': 'input is-primary',
          'placeholder': '********',
        })
