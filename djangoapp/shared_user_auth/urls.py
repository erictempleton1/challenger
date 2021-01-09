from django.urls import include, path
from django.contrib.auth import views as auth_views
from shared_user_auth.views import RegisterView, Profile


app_name = 'shared_user_auth'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', Profile.as_view(), name="profile"),
]

# TODO - create register and profile views. Use challenger repo for examples!
