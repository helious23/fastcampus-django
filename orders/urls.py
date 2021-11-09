from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("shops/", views.shop, name="shop"),
    path("menus/<int:pk>", views.menu, name="menu"),
    path("order/", views.order, name="order"),
]
