from django.contrib import admin

# Register your models here.

from myapps.models import Country, State, District,Bloods_Group,Donors_in_Site,Contact_us



admin.site.register(Bloods_Group)
admin.site.register(Donors_in_Site)
admin.site.register(Contact_us)