from django import forms
from visitor.models import Restaurant, Menu, Gallery


class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator', max_length=25)
    password = forms.CharField(label='Parola', widget=forms.PasswordInput())


class RestaurantEditForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("city", "name")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ("description", "menu_name", "date", "price", "restaurant")
        widgets = {
            'menu_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'menu_name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'menu_description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'menu_date'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'menu_price'}),
            'restaurant': forms.NumberInput(attrs={'type': 'hidden', 'class': 'form-control'})
        }


class MenusForm(forms.Form):
    def __init__(self, instance, *args, **kwargs):
        super(MenusForm, self).__init__(*args, **kwargs)
        self.fields['my_choice_field'] = forms.ChoiceField(
            choices=Menu.objects.filter(restaurant=instance))


class GalleryForm(forms.Form):
    picture = forms.ImageField()