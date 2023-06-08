from django.urls import path
from . import views

app_name='diseasepredict'
urlpatterns = [
    path('heart', views.heart, name="heart"),
    path('diabetes', views.diabetes, name="diabetes"),
    path('breast', views.breast, name="breast"),
    path('disease-home', views.home, name="home"),
]