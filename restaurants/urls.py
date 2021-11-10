from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [
    path("orders/<int:shop_pk>", views.order_list, name="order_list"),
    path("time-input/", views.time_input, name="time_input"),
]
