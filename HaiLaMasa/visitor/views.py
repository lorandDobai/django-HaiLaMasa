from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

def hello(request):
    return render(request, 'home.html')

def city_view(request,city=""):
    return HttpResponse(city)
