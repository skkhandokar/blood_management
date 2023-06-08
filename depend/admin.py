from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Business)
admin.site.register(Package)