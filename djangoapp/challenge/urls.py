from django.urls import include, path
from django.contrib.auth.decorators import login_required
from challenge.views import ChallengeCreateView, ChallengeActivityCreateView, ChallengesView, ChallengeDetailView, ChallengeUpdateView, ChallengeActivityDetailView, ChallengeActivityUpdateView

app_name = 'challenge'
urlpatterns = [
    path("", ChallengesView.as_view(), name="challenges"),
    path(
        "<int:pk>/", 
        ChallengeDetailView.as_view(), 
        name="challenge_detail"),
    path(
        "<int:pk>/update/", 
        login_required(ChallengeUpdateView.as_view()), 
        name="challenge_update"),
    path(
        "create/",
        login_required(ChallengeCreateView.as_view()),
        name="create_challenge"),
    path(
        "<int:pk>/activity/create/",
         login_required(ChallengeActivityCreateView.as_view()),
         name="create_challenge_activity"),
    path(
        "<int:pk>/activity/<int:activity_pk>/",
        login_required(ChallengeActivityDetailView.as_view()),
        name="challenge_activity_detail"),
    path(
        "<int:pk>/activity/<int:activity_pk>/update/",
        login_required(ChallengeActivityUpdateView.as_view()),
        name="challenge_activity_update"),
]
