from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from challenge.models import Challenge


class RegisterView(FormView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/create_user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class Profile(ListView):
    model = Challenge
    template_name = "user/profile.html"
    paginate_by = 10
    context_object_name = "user_created_challenges"

    def get_queryset(self):
        return self.model.objects.filter(creator=self.request.user).order_by('-created')
