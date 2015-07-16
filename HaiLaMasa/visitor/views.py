from django.shortcuts import render
from .models import Restaurant
from django.http import HttpResponse
from datetime import date
# Create your views here.

def hello(request):
    return render(request, 'home.html')

def city_view(request,city=""):
    results = Restaurant.objects.filter(city=city.lower().title())
    return HttpResponse(results)
