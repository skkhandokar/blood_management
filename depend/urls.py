from django.urls import path
from .views import *

app_name='depend'
urlpatterns = [
       path('', dependantfield, name="dependantfield"),
    path('get-states/', get_states, name="get_states"),
    path('get-cities/', get_cities, name="get_cities"),
    path('get-business/', get_business, name="get_business"),
    path('get-packages/', get_package, name="get_package"),

]