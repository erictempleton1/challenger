from django.urls import include, path
from django.contrib.auth import views as auth_views
from shared_user_auth.views import SignupView, Profile
from shared_user_auth.forms import UserLoginForm


app_name = "shared_user_auth"
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(authentication_form=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("profile/", Profile.as_view(), name="profile"),
]