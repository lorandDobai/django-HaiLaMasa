
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.views.generic import ListView
from visitor.models import Restaurant


def login_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        return HttpResponse("Login Failed")

# Create your views here.

@login_required
def resto_selection(request):
    my_restaurants = Restaurant.objects.filter(user = request.user)
    context = Context({"restos": list(my_restaurants)})
    return render(request, "organizer/dashboard_base.html", context)

@login_required
def resto_edit(request, pk=None):
    resto = Restaurant.objects.get(pk = pk)
    context = Context({"resto":resto})
    return render(request,"organizer/restaurant_edit.html",context)
