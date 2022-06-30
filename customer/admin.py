from django import forms
from django.contrib import admin
from .models import Customer

class CustomerForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=30)
    
class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'password', 'confirm_password', 'birthdate'),
        }),
    )

admin.site.register(Customer, CustomerAdmin)
