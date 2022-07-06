from django.contrib import admin
from .models import *


@admin.register(cars_data)
class cd_admin(admin.ModelAdmin):
    search_fields = ['name', 'model', 'color', 'maker', 'registration_no', 'types']
