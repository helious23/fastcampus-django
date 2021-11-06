from django.db import models


class Shops(models.Model):
    shop_name = models.CharField(max_length=50)
    shot_address = models.CharField(max_length=100)


class Menus(models.Model):
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)


class Orders(models.Model):
    pass


class OrderFoodLists(models.Model):
    pass
