from django.urls import path
from deliveries import views

app_name = "deliveries"

urlpatterns = [path("orders/", views.order_list, name="order_list")]
