from django.contrib.auth import login
from django.shortcuts import render, redirect
# Create your views here.

from django.urls import reverse

from home.forms import CustomUserCreationForm


def index(request):
    return render(request, "home/index.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home_page"))
        else:
            # form is invalid, return error
            return render(
                request, "registration/register.html",
                {"form": form}
            )
