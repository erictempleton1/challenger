from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

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


class ChallengesView(ListView):
    model = Challenge
    template_name = 'challenges/challenges.html'
    paginate_by = 10
    context_object_name = "challenges"

    def get_queryset(self):
        return self.model.objects.all().order_by('-created')
