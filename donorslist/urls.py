from django.urls import path
from . import views


app_name='donors'
urlpatterns=[
    path ('',views.donor_in_site_filter,name='donors'),
    path ('pre/',views.donor_in_site_filter,name='pre'),
]