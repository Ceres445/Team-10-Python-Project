from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def index(request):
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
