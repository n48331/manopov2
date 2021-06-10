from django.contrib import admin
from mapbox_location_field.admin import MapAdmin  
from .models import *
# Register your models here.

admin.site.register(search)
admin.site.register(Member)
