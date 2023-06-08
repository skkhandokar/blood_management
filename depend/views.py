from django.shortcuts import render
from requests import request
from .models import State,Country,District,Business,Package
# Create your views here.
from myapps.models import Bloods_Group,Donors_in_Site
from myapps.forms import DonorsState,DonorsDistrict,DonorsCountry
def get_states(request):

    country_id = request.GET.get('country_id')
    print(country_id)
    get_country = Country.objects.get(name=country_id)
    state = State.objects.filter(country=get_country)
    return render(request, 'depend/get-states.html', locals())

def get_cities(request):
    state_id = request.GET.get('state_id')
    get_state = State.objects.get(name=state_id)
    city = District.objects.filter(state=get_state)
    return render(request, 'depend/get-cities.html', locals())

def get_business(request):
    city_id = request.GET.get('city_id')
    get_city = District.objects.get(name=city_id)
    business = Business.objects.filter(city=get_city)
    return render(request, 'depend/get-business.html', locals())

def get_package(request):
    business_id = request.GET['business_id']
    get_business = Business.objects.get(name=business_id)
    package = Package.objects.filter(business=get_business)
    return render(request, 'depend/get-package.html', locals())

from django.contrib.auth.decorators import login_required

def dependantfield(request):
 if request.user.is_authenticated:
    try:
        instance=Donors_in_Site.objects.get(user=request.user)
        if instance:
            country = Country.objects.all()
            bloods= Bloods_Group.objects.all()
            
            district= DonorsDistrict(district_set=District.objects.all().order_by('name'))
            state= DonorsState(state_set=State.objects.all().order_by('name'))
            country= DonorsCountry(country_set=Country.objects.all().order_by('name'))
            return render(request, 'depend/dependantfield.html', locals())           
    except:
        country = Country.objects.all()
        bloods= Bloods_Group.objects.all()
        district= DonorsDistrict(district_set=District.objects.all().order_by('name'))
        state= DonorsState(state_set=State.objects.all().order_by('name'))
        country= DonorsCountry(state_set=Country.objects.all().order_by('name'))
        return render(request, 'depend/dependantfield.html', locals())
 else:
     page = 'login'
     return render(request, 'loginapp/login.html',locals())


# if request.method == 'POST':
#         form = DonorsCountry(request.POST)
#         if form.is_valid():
#             form.save()
#             # redirect to a success page
#         else:
#           form = DonorsCountry()
#         return render(request, 'create_donor.html', {'form': form})