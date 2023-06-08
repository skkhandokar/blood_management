from django import forms
from django.core import validators
from depend.models import Country, State, District


from django import forms
from .models import Donors_in_Site
from .fields import ListTextWidget


class DonorsDistrict(forms.ModelForm ):
    class Meta:
        model = Donors_in_Site
        fields = ['country', 'state', 'district']
        # widgets = {
        #     'country': forms.Select(attrs={'class': 'appearance-none block bg-slate-100 text-black dark:text-white border-2 border-gray-900 rounded-lg py-3 px-5 mb-3 leading-tight focus:outline-none focus:bg-white mr-[200px]'}),
        #     'state': forms.Select(attrs={'class': 'appearance-none block bg-slate-100 text-black dark:text-white border-2 border-gray-900 rounded-lg py-3 px-5 mb-3 leading-tight focus:outline-none focus:bg-white mr-[200px]'}),
        #     'district': forms.Select(attrs={'class': 'appearance-none block bg-slate-100 text-black dark:text-white border-2 border-gray-900 rounded-lg py-3 px-5 mb-3 leading-tight focus:outline-none focus:bg-white mr-[200px]'}),
        # }
        # fields = '__all__'


    def __init__(self,*args,**kwargs):
        _district_set=kwargs.pop('district_set',None)
      
        super(DonorsDistrict,self).__init__(*args,**kwargs)
        self.fields["district"].widget=ListTextWidget(data_pack=_district_set,name='district-set')

#     def __init__(self,*args,**kwargs):
#         _state_set=kwargs.pop('state_set',None)
#         super(DonorsInSiteForm,self).__init__(*args,**kwargs)
#         self.fields["state"].widget=ListTextWidget(data_list=_state_set,name='state-set')


class DonorsState(forms.ModelForm):
    class Meta:
        model = Donors_in_Site
        fields = ['country', 'state', 'district']
        # widgets = {
        #     'country': forms.Select(attrs={'class': 'appearance-none block bg-slate-100 text-black dark:text-white border-2 border-gray-900 rounded-lg py-3 px-5 mb-3 leading-tight focus:outline-none focus:bg-white mr-[200px]'}),
        #     'state': forms.Select(attrs={'class': 'appearance-none block bg-slate-100 text-black dark:text-white border-2 border-gray-900 rounded-lg py-3 px-5 mb-3 leading-tight focus:outline-none focus:bg-white mr-[200px]'}),
        #     'district': forms.Select(attrs={'class': 'appearance-none block bg-slate-100 text-black dark:text-white border-2 border-gray-900 rounded-lg py-3 px-5 mb-3 leading-tight focus:outline-none focus:bg-white mr-[200px]'}),
        # }    
    def __init__(self,*args,**kwargs):
        _state_set=kwargs.pop('state_set',None)
        super(DonorsState,self).__init__(*args,**kwargs)
        self.fields["state"].widget=ListTextWidget(data_pack=_state_set,name='state-set')


class DonorsCountry(forms.ModelForm):
    class Meta:
        model = Donors_in_Site
        fields = ['country', 'state', 'district']
        
    def __init__(self,*args,**kwargs):
        _country_set=kwargs.pop('state_set',None)
        super(DonorsCountry,self).__init__(*args,**kwargs)
        self.fields["country"].widget=ListTextWidget(data_pack=_country_set,name='country-set')