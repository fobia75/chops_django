from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length= 15)
    adress = models.CharField(max_length= 200)
    reg_date = models.DateField(default=timezone.now)


class Product(models.Model):
    name = models.CharField(max_length=100) 
    description= models.TextField() 
    price = models.DecimalField(max_digits= 10 , decimal_places= 2) 
    quaniti = models.IntegerField() 
    aded_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    product = models.ManyToManyField(Product)
    total_price = models.FloatField(blank=False, default=0)
    datetime_of_payment = models.DateTimeField(default=timezone.now)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
