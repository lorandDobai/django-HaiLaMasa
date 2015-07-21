
import json
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.context_processors import csrf
from visitor.models import Restaurant, Menu, Gallery
from organizer.forms import RestaurantEditForm, MenuEditForm, MenusForm, GalleryForm



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

    form = RestaurantEditForm(None,instance = instance)

    context = Context({"resto":instance, "form":form, \
                       "menus":({"name":m.name,"pk":m.pk} for m in Menu.objects.filter(restaurant=instance)), \
                       "gallery": Gallery.objects.filter(restaurant=instance)})
    context.update(csrf(request))
    return render(request, 'organizer/restaurant_edit.html', context)

@login_required
def resto_validate(request):

    data = request.POST

    return HttpResponse(request.POST["name"]+" validam luni aci")

@login_required
def menu_data(request):
    pk_menu=request.GET.get("pk_menu",-1)
    menu = Menu.objects.get(pk=pk_menu)
    result = {"name": menu.name, "description":menu.description,"date": str(menu.date), "price":str(menu.price)}
    data = json.dumps(result)

    return HttpResponse(data)

@login_required
def view_gallery(request):
    if request.method == 'POST':
        form_gallery = GalleryForm(request.POST, request.FILES)
        if form_gallery.is_valid():
            # file is saved
            form_gallery.save()
            return HttpResponseRedirect('')
    else:
        form_gallery = GalleryForm()
    c = {'form_gallery': form_gallery}
    c.update(csrf(request))
    return render(request, 'upload.html', {'form_gallery': form_gallery}, c)

@login_required
def upload_img(request,pk=None):
    data = request.FILES
    image = Gallery(restaurant = Restaurant.objects.get(id=pk))
    img_name = data['file'].name
    image.picture.save(img_name, data['file'], True)
    return HttpResponse("OK")

@login_required
def delete_img(request,pk=None):
    data = request.POST
    Gallery.objects.get(id=data['pk']).delete()
    return HttpResponse("OK")