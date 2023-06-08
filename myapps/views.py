from django.shortcuts import render ,redirect,HttpResponse,HttpResponseRedirect
# from django.views.generic import ListView,DetailView

from myapps.models import  Bloods_Group,Contact_us
from django.views.generic import ListView,DetailView, TemplateView
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages
from myapps.models import Donors_in_Site
from django.core.files.storage import FileSystemStorage
from depend.models import State,Country,District
# Create your views here.

def home(request):
   return render(request,'index.html')

def about_us(request):
   return render(request,'about_us.html')

# def Donor_Registration(request):

#     countryid = request.GET.get('country')

#     stateid = request.GET.get('state')
#     state = None
#     district = None
#     if countryid :
#         getcountry = Country.objects.get(name=countryid)
        
#         state = State.objects.filter(country=getcountry)
#     if stateid:
#         getstate = State.objects.get(name=stateid)
#         district = District.objects.filter(state=getstate)
    
#     country = Country.objects.all()
#     bloods= Bloods_Group.objects.all()


#     return render(request, 'Donor_Registration1.html',locals())




def contact_us(request):
          
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject = request.POST.get('subject', )
        message= request.POST.get('message')
        admin='khandokarsamad4@gmail.com'
        
        if subject and message and email:
           contact=Contact_us(sender_name=name,from_email=email,subject=subject,message=message)
           contact.save()
           send_mail(subject,message,email, [admin,email,name])
           messages.success(request,'Succesfully Send Message!')
        
         
        else:
           messages.error(request,'Make sure all fields are entered and valid!')

    return render(request, 'contact.html')


def Donor_Reg_Site(request):
  print("okk")
  
  if request.method=='POST' :
    country = request.POST.get('country')
    state = request.POST.get('state')
    district = request.POST.get('district')

    if not Country.objects.filter(name=country.title()).exists():
                c=''.join(country)
                c = Country(name=c.title())
                c.save()
                # c=c.capitalize()
                # print(1111111111111111111111)
                # c=Country.objects.create(name=c)
             
                # c.save()
            
    if not State.objects.filter(name=state.title()).exists():
                c = Country.objects.get(name=country.title())
                s = State(name=state.title(), country=c)
          
                s.save()
            #    s=s.capitalize()
            #    c=c.capitalize()
            #    print(22222222222222222)
            #    c = Country.objects.get(name=c)
            #    obj = State(country=c,name=s)
         
            #    obj.save()
    if not District.objects.filter(name=district.title()).exists():
                c = State.objects.get(name=state.title())
                s = District(name=district.title(), state=c )
          
                s.save()
    #            d=''.join(district)
    #            s=''.join(state)
    #            d=d.capitalize()
    #            s=s.capitalize()
    #            obj=District.objects.create(state=s,name=d)
    #            obj=obj.capitalize()
    #            obj.save()
    try:   
        instance=Donors_in_Site.objects.get(user=request.user)
        
        if instance:
            instance.user=request.user
            phone = request.POST['phone']
            phone_str = ''.join(phone)
            instance.phone = phone_str

            blood = request.POST.get('blood'),
            blood_str = ''.join(blood)
            instance.blood=blood_str

            dob=request.POST['dob'],
            dob_str=''.join(dob)
            instance.Last_Donate = dob_str
        
            country = request.POST.get('country'),
            country_str=''.join(country)
            country_str=country_str.title()
            instance.country = country_str

            state = request.POST.get('state'),
            state_str=''.join(state)
            state_str=state_str.title()
            instance.state = state_str

            district = request.POST.get('district'),
            district_str=''.join(district)
            district_str=district_str.title()
            instance.district = district_str
        
            if len(request.FILES) == 0:
                print('no files')
            else: 
                _, file = request.FILES.popitem()
                file = file[0]
                instance.image = file
                instance.save()
        
            instance.save()
            
           
            messages.success(request,'Data has been updated!')
            return render(request, 'index.html')
    except:
        en=Donors_in_Site.objects.create(
        user=request.user,
        phone = request.POST['phone'],
        blood = request.POST.get('blood' ),
        Last_Donate = request.POST['dob'],
    
        country = request.POST.get('country').title(),
       
        state = request.POST.get('state').title(),
        district = request.POST.get('district').title()
          )
        if len(request.FILES) == 0:
            print('no files')
        else: 
            _, file = request.FILES.popitem()
            file = file[0]
            en.image = file
            en.save()

       
        print("okk")
        messages.success(request,'Data has been submitted!')
        return render(request, 'index.html')
 
        
  else:
        messages.error(request,'something mistake.please Reloade and try again!!')
        return render(request, 'dependantfield.html')
        
# Create your views here.

class donor(DetailView):
      model=Donors_in_Site
      template_name='loginapp/profile2.html'
      context_object_name='user'