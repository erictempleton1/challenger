from django.urls import include, path
from django.contrib.auth.decorators import login_required
import challenge.views as challenge_views

app_name = 'challenge'
urlpatterns = [
    path("", challenge_views.ChallengesView.as_view(), name="challenges"),
    path(
        "<int:pk>/",
        challenge_views.ChallengeDetailView.as_view(),
        name="challenge_detail"),
    path(
        "<int:pk>/update/",
        login_required(challenge_views.ChallengeUpdateView.as_view()),
        name="challenge_update"),
    path(
        "create/",
        login_required(challenge_views.ChallengeCreateView.as_view()),
        name="create_challenge"),
    path(
        "<int:pk>/delete/",
        login_required(challenge_views.ChallengeDeleteView.as_view()),
        name="challenge_delete"),
    path(
        "<int:pk>/activity/create/",
        login_required(challenge_views.ActivityCreateView.as_view()),
        name="create_challenge_activity"),
    path(
        "activity/<int:pk>/",
        login_required(challenge_views.ActivityDetailView.as_view()),
        name="activity_detail"),
    path(
        "activity/<int:pk>/update/",
        login_required(challenge_views.ActivityUpdateView.as_view()),
        name="activity_update"),
    path(
        "activity/<int:pk>/delete/",
        login_required(challenge_views.ActivityDeleteView.as_view()),
        name="activity_delete")
]
