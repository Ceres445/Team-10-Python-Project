from django.contrib.auth import login
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

import home.forms as forms


def index(request):
    return render(request, "home/index.html")
    # rick roll
    # return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


def register(request):
    if request.method == "GET":
        # User is trying to login
        return render(
            request, "home/register.html",
            {"form": forms.CustomUserCreationForm}
        )
    elif request.method == "POST":
        # User has submitted login details
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home_page"))
        else:
            # form is invalid, return error
            return render(
                request, "home/register.html",
                {"form": form}
            )