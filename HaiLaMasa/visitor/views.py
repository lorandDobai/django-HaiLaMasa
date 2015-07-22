from django.shortcuts import render, render_to_response
from django.template import Context, Template, RequestContext
from django.template.context_processors import csrf
from .models import Restaurant, Menu
import datetime
from django.http import HttpResponse
from datetime import date
# Create your views here.

def hello(request):
    return render(request, 'visitor/home.html')

def city_view(request,city=""):
    menus = Menu.objects.filter(date__exact=datetime.date.today(),restaurant__city=city.lower().title())
    context_dict = {"menus": list(menus)}
    context_dict.update(csrf(request))
    #context = Context(context_dict)

    #return render(request, "visitor/base_oras.html", context)
    return render_to_response('visitor/base_oras.html', context_dict, context_instance=RequestContext(request))


