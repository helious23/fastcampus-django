from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponse
from orders.models import Order, Shop


@csrf_exempt
def order_list(request, shop_pk):
    if request.method == "GET":
        order_list = Order.objects.filter(shop=shop_pk)
        shop = Shop.objects.get(pk=shop_pk)
        return render(
            request,
            "restaurant/restaurant_order_list.html",
            {"order_list": order_list, "shop": shop},
        )
    else:
        return HttpResponse(status=404)


def time_input(request):
    if request.method == "POST":
        estimated_time = request.POST.get("estimated_time")
        order_id = int(request.POST.get("order_id"))
        order_item = Order.objects.get(pk=order_id)
        shop_pk = order_item.shop.pk
        order_item.estimated_time = estimated_time
        order_item.save()
        messages.success(request, "Estimating time is changed")
        return redirect(reverse("restaurants:order_list", kwargs={"shop_pk": shop_pk}))
    else:
        return HttpResponse(status=404)
