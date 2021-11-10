from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponse
from orders.models import Order


@csrf_exempt
def order_list(request):
    if request.method == "GET":
        order_list = Order.objects.all()
        return render(
            request,
            "delivery/delivery_order_list.html",
            {"order_list": order_list},
        )
    elif request.method == "POST":
        order_id = int(request.POST.get("order_id"))
        order_item = Order.objects.get(pk=order_id)
        order_item.deliver_finished = True
        order_item.save()
        messages.success(request, "Delivery Finished")
        return redirect(reverse("deliveries:order_list"))
    else:
        return HttpResponse(status=404)
