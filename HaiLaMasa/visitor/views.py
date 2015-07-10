from django.shortcuts import render
from django.http import HttpResponse
from visitor.models import  Restaurant
# Create your views here.


def hello(request):
    rest = Restaurant.objects.create(
        name = "Eli",
    )
    rest.save()
    return HttpResponse("Hello Mancare!");
