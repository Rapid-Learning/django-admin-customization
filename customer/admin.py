from django import forms
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '//code.jquery.com/jquery-3.6.0.min.js',
            'customer/custom.js',
        )

admin.site.register(Customer, CustomerAdmin)
