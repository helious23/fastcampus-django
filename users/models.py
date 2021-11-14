from django.db import models


class User(models.Model):

    CUSTOMER = 0
    OWNER = 1
    DELIVERY = 2
    USER_ROLE = (
        (CUSTOMER, "Customer"),
        (OWNER, "Owner"),
        (DELIVERY, "Delivery"),
    )

    user_name = models.CharField(max_length=20)
    user_type = models.IntegerField(choices=USER_ROLE)
