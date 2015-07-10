from django.shortcuts import render
from django.http import HttpResponse
from visitor.models import  Restaurant
from datetime import date
# Create your views here.


def hello(request):
    return render(request, 'test.html' )
