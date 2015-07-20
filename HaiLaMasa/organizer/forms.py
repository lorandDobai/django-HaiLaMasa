
from django import forms
from visitor.models import Restaurant, Menu, Gallery

class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator', max_length=25)
    password = forms.CharField(label='Parola',widget = forms.PasswordInput())

class RestaurantEditForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("city","name")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields =("description","picture","name","date","price")

class MenusForm(forms.Form):
     def __init__(self, instance, *args, **kwargs):
        super(MenusForm, self).__init__(*args, **kwargs)
        self.fields['my_choice_field'] = forms.ChoiceField(
            choices=Menu.objects.filter(restaurant=instance))

class GalleryForm(forms.Form):
    picture = forms.ImageField()