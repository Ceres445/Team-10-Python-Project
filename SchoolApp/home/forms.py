from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from home.models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class AvatarChangeForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
