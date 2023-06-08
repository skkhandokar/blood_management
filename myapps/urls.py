
# from django import views
from django.urls import path
from . import views


app_name='myapp'
urlpatterns=[
    path ('',views.home,name='home'),
    path ('about_us/',views.about_us,name='about_us'),
    # path ('donorform/',views.Donor_Registration,name='Donor_Registration'),
    path ('contact-us/',views.contact_us,name='contact_us'),
   
    # path ('send-mail/',views.sendmail,name='send-mail'),
    path ('donor-reg-site/',views.Donor_Reg_Site,name='donor-reg-site'),
    path ('donor/<slug>/',views.donor.as_view(),name='donor_details'),
    


]