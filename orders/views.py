from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from orders.models import OrderFoodList, Shop, Menu, Order
from orders.serializers import MenuSerializer, ShopSerializer


@csrf_exempt
def shop(request):
    if request.method == "GET":
        shops = Shop.objects.all()

        # serializer = ShopSerializer(shops, many=True)
        # return JsonResponse(serializer.data, safe=False)

        return render(request, "order/shop_list.html", {"shop_list": shops})

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def menu(request, pk):
    if request.method == "GET":
        menus = Menu.objects.filter(shop=pk)

        # serializer = MenuSerializer(menus, many=True)
        # return JsonResponse(serializer.data, safe=False)

        return render(
            request, "order/menu_list.html", {"menu_list": menus, "shop_pk": pk}
        )

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def order(request):
    if request.method == "POST":
        address = request.POST.get("address")
        shop = int(request.POST.get("shop"))
        food_list = request.POST.getlist("menu")
        order_date = timezone.now()
        shop_item = Shop.objects.get(pk=shop)
        shop_item.orders.create(address=address, order_date=order_date, shop=int(shop))
        order_item = Order.objects.get(pk=shop_item.orders.latest("pk").pk)
        for food in food_list:
            order_item.order_food_lists.create(food_name=food)
        messages.success(request, "Success to order")

        return redirect(reverse("orders:order"))

    elif request.method == "GET":
        order_list = Order.objects.all()
        order_item = OrderFoodList.objects.all()
        return render(
            request,
            "order/order_list.html",
            {"order_list": order_list, "order_item": order_item},
        )
