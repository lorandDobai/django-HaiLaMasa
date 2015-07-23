from django import template
from ..models import Restaurant, Contact, Address, Gallery

register = template.Library();

@register.filter()
def get_contact_of_restaurant(value):
    try:
        contact = Contact.objects.get(restaurant=value)
    except Contact.DoesNotExist:
        contact = None
    return contact

@register.filter()
def get_address_of_restaurant(value):
    try:
        address = Address.objects.get(restaurant=value)
    except Address.DoesNotExist:
        address = None
    return address


@register.filter()
def get_gallery_of_restaurant(value):
    try:
        gallery = Gallery.objects.filter(restaurant=value)
    except Gallery.DoesNotExist:
        gallery = None
    return gallery