from django.contrib import admin
from django import forms
from .models import Furniture

class FurnitureAdminForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = '__all__'

class FurnitureAdmin(admin.ModelAdmin):
    form = FurnitureAdminForm
    list_display = ('name', 'style', 'height', 'width', 'depth')
    search_fields = ('name', 'style')

admin.site.register(Furniture, FurnitureAdmin)