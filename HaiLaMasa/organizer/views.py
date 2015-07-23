import json
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.context_processors import csrf
from visitor.models import Restaurant, Menu, Gallery,Contact, Address
from organizer.forms import RestaurantEditForm, MenuEditForm, MenusForm, GalleryForm, ContactForm,AddressForm


def login_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        return HttpResponse("Login Failed")


# Create your views here.

@login_required
def resto_selection(request):
    my_restaurants = Restaurant.objects.filter(user=request.user)
    context_dict = {"restos": list(my_restaurants)}
    context_dict.update(csrf(request))

    return render_to_response('organizer/dashboard_base.html', context_dict, context_instance=RequestContext(request))


@login_required
def resto_edit(request, pk=None):

    instance = get_object_or_404(Restaurant, id=pk)

    resto = instance

    form = RestaurantEditForm(None, instance=instance)
    menu_form = MenuEditForm()
    menu_form.restaurant = instance

    contact = Contact.objects.get(restaurant = resto)
    contact_form = ContactForm(None, instance = contact)

    address_form = AddressForm(None, instance = Address.objects.get(restaurant=instance))
    context_dict = {"resto": instance, "form": form, "menu_form": menu_form,
                    "menus": ({"name": m.menu_name, "pk": m.pk} for m in Menu.objects.filter(restaurant=instance)),
                    "gallery": Gallery.objects.filter(restaurant=instance), "contact_form": contact_form,
                    "address_form": address_form
                    }
    context_dict.update(csrf(request))

    return render_to_response('organizer/restaurant_edit.html', context_dict, context_instance=RequestContext(request))


@login_required
def resto_validate(request):
    if request.method == 'POST':

        restaurant = Restaurant.objects.get(id=request.POST['restaurant'])
        restaurant_form = RestaurantEditForm(request.POST, instance = restaurant)
        if restaurant_form.is_valid():
            restaurant_form.save()

        menu = Menu.objects.get(id=request.POST['menu']) if request.POST['menu'] else None
        menu_form = MenuEditForm(request.POST,instance = menu)
        if menu_form.is_valid():
            menu_form.save()

        contact_form = ContactForm(request.POST, instance = Contact.objects.get(restaurant=restaurant))
        if contact_form.is_valid():
            contact_form.save()

        address_form = AddressForm(request.POST, instance = Address.objects.get(restaurant=restaurant))
        if address_form.is_valid():
            address_form.save()

    return HttpResponseRedirect(reverse_lazy('resto-list'))



@login_required
def menu_data(request):
    pk_menu = request.GET.get("pk_menu", -1)
    menu = Menu.objects.get(pk=pk_menu)
    result = {"pk":pk_menu,"name": menu.menu_name, "description": menu.description, "date": str(menu.date), "price": str(menu.price)}
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
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))

@login_required
def upload_img(request,pk=None):
    data = request.FILES
    image = Gallery(restaurant = Restaurant.objects.get(id=pk))
    img_name = data['file'].name
    image.picture.save(img_name, data['file'], True)
    result = {'path': image.picture.url,'pk': image.pk}
    return HttpResponse(json.dumps(result))

@login_required
def delete_img(request,pk=None):
    data = request.POST
    Gallery.objects.get(id=data['pk']).delete()
    return HttpResponse("OK")

