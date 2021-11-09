from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [path("time-input/", views.time_input, name="time_input")]
