from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from orders.models import OrderFoodList, Order


@csrf_exempt
def time_input(request):
    if request.method == "GET":
        order_list = Order.objects.all()
        order_item = OrderFoodList.objects.all()
        return render(
            request,
            "restaurant/restaurant_order_list.html",
            {"order_list": order_list, "order_item": order_item},
        )
    elif request.method == "POST":
        estimated_time = request.POST.get("estimated_time")
        order_id = int(request.POST.get("order_id"))
        order_item = Order.objects.get(pk=order_id)
        order_item.estimated_time = estimated_time
        order_item.save()
        messages.success(request, "Estimating time is changed")
        return redirect(reverse("restaurants:time_input"))
