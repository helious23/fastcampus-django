from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurants.urls", namespace="restaurants")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
