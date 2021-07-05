from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.

from django.urls import reverse

from home.forms import CustomUserCreationForm, AvatarChangeForm


def index(request):
    return render(request, "home/index.html")
    # rick roll
    # return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


def register(request):
    if request.method == "GET":
        # User is trying to login
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        # User has submitted login details
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


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'home/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('home:view_profile'))
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'home/edit_profile.html', args)


def change_avatar(request):
    if request.method == 'POST':
        form = AvatarChangeForm(request.POST, request.FILES,
                                instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = AvatarChangeForm(instance=request.user.profile)

    return render(request, 'home/avatar_change.html', {'form': form})
