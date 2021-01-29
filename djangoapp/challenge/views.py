from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

from challenge.models import Challenge, Activity
from challenge.forms import ChallengeForm, ActivityForm


class ChallengeCreateView(CreateView):
    model = Challenge
    template_name_suffix = "_create_form"
    success_url = reverse_lazy('challenge:challenges')
    form_class = ChallengeForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        form.instance.members.add(self.request.user)
        return super().form_valid(form)


class ChallengesView(ListView):
    model = Challenge
    paginate_by = 30
    context_object_name = "challenges"

    def get_queryset(self):
        return self.model.objects.all().order_by('-created')


class ChallengeDetailView(DetailView):
    model = Challenge
    context_object_name = "challenge"


class ChallengeUpdateView(UserPassesTestMixin, UpdateView):
    model = Challenge
    template_name_suffix = "_update_form"
    form_class = ChallengeForm

    def test_func(self):
        challenge = self.get_object()
        return self.request.user == challenge.created_by

    def get_success_url(self):
        return reverse_lazy('challenge:challenge_detail', kwargs={'pk': self.object.pk})


class ChallengeActivityCreateView(CreateView):
    model = Activity
    # fields = ["activity", "distance", "measure", "hours", "minutes", "seconds"]
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("challenge:challenges")
    form_class = ActivityForm

    def form_valid(self, form):
        form.instance.challenge = Challenge.objects.get(pk=self.kwargs["pk"])
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ChallengeActivityDetailView(DetailView):
    model = Activity
    context_object_name = "activity"


class ChallengeActivityUpdateView(UpdateView):
    model = Activity
    template_name_suffix = "_update_form"
    form_class = ActivityForm


    def test_func(self):
        activity = self.get_object()
        return self.request.user == activity.created_by
    
    def get_success_url(self):
        return reverse_lazy('challenge:activity_detail', kwargs={'pk': self.object.pk})
