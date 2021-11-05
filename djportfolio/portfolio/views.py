from django.shortcuts import render
from .models import User


def index(request):
    user = User.objects.filter()

    return render(request, 'index.html')
