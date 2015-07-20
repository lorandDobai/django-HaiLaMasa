
from django import forms
from visitor.models import Restaurant, Menu

class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator', max_length=25)
    password = forms.CharField(label='Parola',widget = forms.PasswordInput())

class RestaurantEditForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("city","name")

class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields =("description","picture","name","date","price")

class MenusForm(forms.Form):
     def __init__(self, instance, *args, **kwargs):
        super(MenusForm, self).__init__(*args, **kwargs)
        self.fields['my_choice_field'] = forms.ChoiceField(
            choices=Menu.objects.filter(restaurant=instance))