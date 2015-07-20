
import json
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.context_processors import csrf
from visitor.models import Restaurant, Menu
from organizer.forms import RestaurantEditForm, MenuEditForm, MenusForm



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
    instance = get_object_or_404(Restaurant, id=pk)

    form = RestaurantEditForm( None,instance = instance)
    menus_form = MenusForm(instance)
    context = Context({"resto":instance, "form":form, "menus":Menu.objects.filter(restaurant=instance)})
    context.update(csrf(request))
    return render(request, 'organizer/restaurant_edit.html', context)

@login_required
def resto_validate(request):
    return HttpResponse(request.POST["name"]+" validam luni aci")
@login_required
def menu_data(request,pk_rest=None,pk_menu=None):

    menu = Menu.objects.filter(pk=pk_menu)
    #result = {"name": menu.name, "description":menu.description,"date":menu.date, "price":menu.price}
    result = menu.__dict__
    data = json.dumps(result)
    return HttpResponse(result)

