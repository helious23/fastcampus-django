from django.contrib import admin
from . import models


@admin.register(models.Order)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Shop)
class ShopsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Menu)
class MenusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderFoodList)
class OrderFoodListAdmin(admin.ModelAdmin):
    pass
