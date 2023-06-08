# from django.urls import path
# from . import views


# app_name='loginapp'
# urlpatterns=[
#     path ('',views.loginuser,name='loginuser'),
#     path ('logout/',views.logoutuser,name='logoutuser'),
#     path ('signup',views.registration,name='signup'),
  
  
# ]

app_name='loginapp'
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('registration/', views.userRegister, name='registration'),
    path('change_passward/', views.change_passward, name='change_passward'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('edit-user-profile/', views.EditUserProfile, name='EditUserProfile'),
    path('profile/', views.profile, name='profile'),
    # path('profile/<int:pk>/', views.UpdateViewProfile.as_view(), name='profile_update'),
    path('user/<slug>/', views.UserProfileDetailView.as_view(), name='user_profile'),
    path('user_delete/<int:pk>/', views.DeleteUser.as_view(), name='user_delete'),
  
]
