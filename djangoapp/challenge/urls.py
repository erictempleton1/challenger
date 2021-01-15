from django.urls import include, path
from django.contrib.auth.decorators import login_required
from challenge.views import ChallengeCreateView, ChallengeActivityCreateView, ChallengesView, ChallengeDetailView


app_name = 'shared_user_auth'
urlpatterns = [
    path("", ChallengesView.as_view(), name="challenges"),
    path("<int:pk>/",ChallengeDetailView.as_view(), name="challenge"),
    path(
        "create/",
        login_required(ChallengeCreateView.as_view()),
        name="create_challenge"),
    path(
        "<int:pk>/activity/create",
        login_required(ChallengeActivityCreateView.as_view()),
        name="create_challenge_activity")
]
