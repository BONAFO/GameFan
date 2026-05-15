from django.urls import path
from .views import SignUpView, LogoutView, LoginView

app_name = "users"

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("login", LoginView.as_view(), name="login"),
]
