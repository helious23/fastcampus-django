from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from rest_framework.parsers import JSONParser
from users.serializers import UserSerializer
from users.models import User


@csrf_exempt
def user(request):
    if request.method == "GET":
        users = User.objects.all()
        return render(request, "users/user_list.html", {"user_list": users})
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "users/login.html")

    elif request.method == "POST":
        name = request.POST.get("name")
        try:
            user = User.objects.get(user_name=name)
            request.session["user_id"] = user.id
            print(request.session["user_id"])
            messages.success(request, f"Welcome {user.user_name}")
            return redirect(reverse("orders:order"))
        except User.DoesNotExist:
            messages.error(request, f"{name} not found")
            return redirect(reverse("users:login"))
