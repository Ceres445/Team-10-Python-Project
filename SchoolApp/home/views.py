from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe

from home.forms import CustomUserCreationForm, AvatarChangeForm, CustomUserChangeForm
# TODO: add class creation request
from public_api.models import Post, Comment


# Create your views here.


def index(request):
    # rick roll
    # return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    if request.user.is_authenticated:
        return render(request, "home/index.html",
                      {
                          'courses': list(map(str, request.user.profile.courses.all()))
                      })
    else:
        return render(request, "home/index.html")


def register(request):
    if request.method == "GET":
        creation_form = CustomUserCreationForm
    elif request.method == "POST":
        # User has submitted login details
        creation_form = CustomUserCreationForm(request.POST)
        if creation_form.is_valid():
            user = creation_form.save()
            login(request, user)
            return redirect(reverse("homePage"))
    else:
        return HttpResponseForbidden(f"Method {request.method} not allowed")
    return render(
                request, "registration/register.html",
                {"form": creation_form}
            )


# DONE: ability to see others profiles
@login_required
def view_profile(request, username=None):
    current = False
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
        current = True

    args = {'user': user, 'courses': ", ".join(list(map(str, user.profile.courses.all()))), 'current': current}
    return render(request, 'home/profile.html', args)


@login_required
def edit_profile(request):
    """Edit your profile"""
    second_form = AvatarChangeForm(instance=request.user.profile)
    if request.method == 'POST':
        first_form = CustomUserChangeForm(request.POST, instance=request.user)
        if first_form.is_valid():
            first_form.save()
            return redirect(reverse('profile'))
    else:
        first_form = CustomUserChangeForm(instance=request.user)

    return render(request, 'home/edit_profile.html', {'form': first_form, 'second_form': second_form, 'files': True})


@login_required
def change_avatar(request):
    """Form to change avatar/profile (rename needed)"""

    if request.method == 'POST':
        form = AvatarChangeForm(request.POST, request.FILES,
                                instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = AvatarChangeForm(instance=request.user.profile)

    return render(request, 'home/avatar_change.html', {'form': form})


def view_post_detail(request, pk=1):
    """See a post in detail with comments and links"""
    post = get_object_or_404(Post, pk=pk)  # raise 404 if invalid user
    comments = Comment.objects.all().filter(post__id=post.id)
    return render(request, 'home/posts_detail.html', {"pk": mark_safe(pk),
                                                      'post': post, 'user': request.user,
                                                      'comments': comments,
                                                      'author': post.author})


def view_posts(request):
    """See all posts """
    if request.user.is_authenticated:
        return render(request, "home/posts.html",
                      {
                          'courses': list(map(str, request.user.profile.courses.all()))
                      })
    else:
        return render(request, "home/posts.html")


def view_user_posts(request, pk=None):
    """View your own posts or others posts"""
    if pk is None:
        pk = request.user.pk

    user = get_object_or_404(User, pk=pk)
    return render(request, 'home/view_user_posts.html', {"pk": user.username, "user": user})
