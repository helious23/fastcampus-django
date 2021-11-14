from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("deliveries/", include("deliveries.urls", namespace="deliveries")),
    path("restaurant/", include("restaurants.urls", namespace="restaurants")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
