from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from shared_user_auth.forms import CustomUserCreationForm


class SignupView(FormView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('shared_user_auth:profile')
    template_name = 'registration/create_user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class Profile(TemplateView):
    template_name = "user/profile.html"
