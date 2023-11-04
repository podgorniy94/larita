from django.http import HttpResponse  # Temp
from django.shortcuts import render


def index(request):
    return HttpResponse("HelloWorld")
