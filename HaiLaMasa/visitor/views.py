from django.shortcuts import render
from django.template import Context, Template
from .models import Restaurant, Menu
import datetime
from django.http import HttpResponse
from datetime import date
# Create your views here.

def hello(request):
    return render(request, 'visitor/home.html')

def city_view(request,city=""):
    menus = Menu.objects.filter(date__exact=datetime.date.today(),restaurant__city=city.lower().title())
    context = Context({"menus": list(menus)})
    return render(request, "visitor/base_oras.html", context)

