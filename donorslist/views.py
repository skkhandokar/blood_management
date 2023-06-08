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
import math




def donor_in_site_filter(request):
   
       country= request.POST.get('country')
       state= request.POST.get('state')
       district= request.POST.get('district')
       blood= request.POST.get("blood")

       if  country and blood : 
           if  country !='Choose a Country' and blood =='Blood Type' or country =='Choose a Country' and blood !='Blood Type' :  
               messages.error(request,"At least select country and blood type")              
               return render (request,'donorslist.html' )
       
       if   country and blood  : 
         if country=='Choose a Country':
           if blood =='Blood Type' or 'ALL' or 'A+' or 'B+' or 'AB+' or 'O+'or 'A-'or 'B-'or 'O-'or 'AB-':           
              messages.error(request,"At least select country and blood type")            
              return render (request,'donorslist.html' )
           
       if  country and blood :
          if country !='Choose a Country' and blood !='Blood Type':
              donor_list=Donors_in_Site.objects.filter(blood=blood,country=country).order_by('-created')
              if blood =='ALL':
                 donor_list=  Donors_in_Site.objects.filter(country=country).order_by('-created')
                  

       if  country and state and blood : 
           if country !='Choose a Country' and state !='Choose a State' and blood !='Blood Type':
               donor_list=Donors_in_Site.objects.filter(blood=blood,country=country,state=state).order_by('-created')
               if blood =='ALL':
                   donor_list=Donors_in_Site.objects.filter(country=country,state=state).order_by('-created')
                   pre=donor_list
       if  country and state and district and blood:
           if country !='Choose a Country' and state !='Choose a State'and district!='Choose a District' and blood !='Blood Type':
                donor_list=Donors_in_Site.objects.filter(blood=blood,country=country,state=state,district=district).order_by('-created')
                if blood =='ALL':
                   donor_list=Donors_in_Site.objects.filter(country=country,state=state).order_by('-created')
                   pre=donor_list
       else:
          donor_list=[]
     
       length=len(donor_list)
       if length>=100:
                show=20
           
       elif length>=50:
                show=12
              
       elif length>=10:
                show=8
             
       else:
                show=4
    
       paginator=Paginator(donor_list,show)  
       page_number=request.GET.get('page')
       page=paginator.get_page(page_number)
       donor_list_page=paginator.get_page(page_number)
       custom_range, donorss =paginationProject(request,donor_list,show) 
     
       countryid = request.GET.get('country')
       stateid = request.GET.get('state')
       state = None
       district = None
       if countryid :
        getcountry = Country.objects.get(name=countryid)
                
        state = State.objects.filter(country=getcountry)
       if stateid:
                getstate = State.objects.get(name=stateid)
                district = District.objects.filter(state=getstate)
            
       country = Country.objects.all()
       bloods=   Bloods_Group.objects.all()

       return render(request, 'donorslist.html',locals())      
      
    #   unique charcter search
    #   if country and blood:
    #      if country !='Choose a Country' and blood !='Blood Type':
    #           results=Donors_in_Site.objects.filter(blood=blood,country=country)
    #           queryset=(Q(country__icontains=country)) & (Q(blood__icontains=blood)) 
    #           results=Donors_in_Site.objects.filter(queryset).distinct()
    #           print('country and blood')
    #   if country and state and blood:
    #      if country !='Choose a Country' and state !='Choose a State' and blood !='Blood Type':
    #               queryset=(Q(country__icontains=country)) & (Q(state__icontains=state)) & (Q(blood__icontains=blood))
    #               results=Donors_in_Site.objects.filter(queryset).distinct()
    #               print ('country state blood' )
    #   if  country and state and district and blood:
    #     if country !='Choose a Country' and state !='Choose a State'and district!='Choose a District' and blood !='Blood Type':
                    
    #                   queryset=(Q(country__icontains=country)) & (Q(state__icontains=state)) & (Q(district__icontains=district)) & (Q(blood__icontains=blood))
    #                   results=Donors_in_Site.objects.filter(queryset).distinct()
    #                   print ('country state district blood' )     
    #   else:
    #      results=[]
    #   le=len(results)
    #   return render (request,'donorslist.html',locals())
