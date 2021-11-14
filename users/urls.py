from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("user/", views.user, name="user"),
    path("login/", views.login, name="login"),
]
