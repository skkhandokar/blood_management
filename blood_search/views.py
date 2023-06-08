from django.shortcuts import render ,redirect,HttpResponse,HttpResponseRedirect
# from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from myapps.models import Bloods_Group,Donors_in_Site
from django.views.generic import ListView,DetailView, TemplateView,View
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages
from depend.models import State,Country,District
from django.core.paginator import Paginator
from django.db.models import Q
from .utils import paginationProject
# Create your views here.
import math

def blood_search_filter(request):


   countryid = request.GET.get('country')

   stateid = request.GET.get('state')
   state = None
   district = None

   if countryid :
        getcountry = Country.objects.get(name=countryid)
        
        state = State.objects.filter(country=getcountry )
   if stateid:
          getstate = State.objects.get(name=stateid)
          district = District.objects.filter(state=getstate) 
    
   donor_list= Donors_in_Site.objects.all().order_by('-created')
   length=len(donor_list)
   if length>=100:
                show=20
            
   elif length>=50:
                show=12
               
   elif length>=10:
                show=8
         
   else:
                show=4
           

   country = Country.objects.all()
   bloods= Bloods_Group.objects.all()
   
   paginator=Paginator(donor_list,show)
        
   page_number=request.GET.get('page')
   page=paginator.get_page(page_number)
   donor_list_page=paginator.get_page(page_number)
   custom_range, donorss =paginationProject(request,donor_list,show) 
   return render(request,'blood_search_filter.html',locals() )



 