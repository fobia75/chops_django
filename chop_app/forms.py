from django.forms import ModelForm

from .models import Product, User

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'quaniti',
            'aded_date',
            'image',
        ]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'phone_number',
            'adress',
            'reg_date',
        ]

