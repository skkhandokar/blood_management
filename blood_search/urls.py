from django.urls import path
from . import views


app_name='blood_search'
urlpatterns=[
    path ('',views.blood_search_filter,name='blood-search-filter'),

    

]