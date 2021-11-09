from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=100)

    def __str__(self):
        return self.shop_name


class Menu(models.Model):
    food_name = models.CharField(max_length=20)
    shop = models.ForeignKey(Shop, related_name="menus", on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name


class Order(models.Model):
    address = models.CharField(max_length=120)
    order_date = models.DateTimeField("date ordered")
    estimated_time = models.IntegerField(default=-1)
    deliver_finished = models.BooleanField(default=False)
    shop = models.ForeignKey(Shop, related_name="orders", on_delete=models.CASCADE)

    def __str__(self):
        return f"Address: {self.address} Shop: {self.shop.shop_name}"


class OrderFoodList(models.Model):
    food_name = models.CharField(max_length=20)
    order = models.ForeignKey(
        Order, related_name="order_food_lists", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.food_name
