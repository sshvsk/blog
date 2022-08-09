from urllib import request
import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.forms import RegisterForm
from django.contrib.auth.models import User
from django.conf import settings



logger = logging.getLogger(__name__)

def index_profiles(request):
    # Проверяем GET параметры и собираем сообщение
    message = []
    for key, value in request.GET.items():
        message.append(f"{key}={value}")

    # Проверяем POST параметры и выводим в консоль
    for key, value in request.POST.items():
        logger.info(f"POST param: {key}={value}")

    # Если были GET параметры в запросе, выводим соответствующее сообщение
    if len(message):
        return HttpResponse(f"Profile view with GET params: {', '.join(message)}")
    return HttpResponse("Profile view")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})
