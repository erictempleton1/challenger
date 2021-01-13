from django.urls import include, path
from django.contrib.auth.decorators import login_required
from challenge.views import ChallengeCreateView, ChallengeActivityCreateView, ChallengesView


app_name = 'shared_user_auth'
urlpatterns = [
    path("", ChallengesView.as_view(), name="challenges"),
    path(
        "create/",
        login_required(ChallengeCreateView.as_view()),
        name="create_challenge"),
    path(
        "activity/create",
        login_required(ChallengeActivityCreateView.as_view()),
        name="create_challenge_activity")
]
