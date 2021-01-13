from django.shortcuts import render
from django.views.generic.edit import CreateView

from challenge.models import Challenge, ChallengeActivity


class ChallengeCreateView(CreateView):
  model = Challenge
  fields = ["name"]
  template_name_suffix = "_create_form"

  def form_valid(self, form):
    form.instance.creator = self.request.user
    form.save()
    form.instance.members.add(self.request.user)
    return super().form_valid(form)


class ChallengeActivityCreateView(CreateView):
  model = ChallengeActivity
  fields = ["challenge", "activity"]
  template_name_suffix = "_create_form"

