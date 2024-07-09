from django.http import  HttpResponse
from .models import Image
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserForm, ProductForm
from .models import User, Product

def index(request):
     return render(request, 'index.html')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            adress = form.cleaned_data['adress']
            reg_date = form.cleaned_data['reg_date']

            user = User(name=name, email=email, phone_number= phone_number, adress= adress, reg_date= reg_date)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'user_form.html', {'form':
        form, 'message': message})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quaniti = form.cleaned_data['quaniti']
            aded_date = form.cleaned_data['aded_date']
            image = form.cleaned_data['image']

            product = Product(name=name, description = description, price= price, quaniti= quaniti, aded_date= aded_date,image= image)
            product.save()
            message = 'Продукт сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'product_form.html', {'form':
        form, 'message': message})

