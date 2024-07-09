from django.contrib import admin
from .models import User, Product, Order, Image

class AdminUser(admin.ModelAdmin):
    list_display = ('name','email', 'phone_number', 'adress', 'reg_date',)
    list_filter = ('name',)
    search_fields = ('name','reg_date',)


class AdminProduct(admin.ModelAdmin):
    list_display = ('name','description', 'price', 'quaniti', 'aded_date', 'image',)
    list_filter = ('name',)
    search_fields = ('name','aded_date',)


class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'datetime_of_payment', )
    list_filter = ('user',)
    search_fields = ('user','datetime_of_payment',)


class AdminImage(admin.ModelAdmin):
    list_display = ('title','image',)
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(User, AdminUser)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
admin.site.register(Image, AdminImage)
