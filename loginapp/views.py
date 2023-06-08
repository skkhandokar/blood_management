from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .forms import UserProfileForm
from .models import UserProfile
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.http import HttpResponse
#email verify
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
#delete user
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView

UserModel=get_user_model()

def userLogin(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('myapp:home')      

    if request.method=='POST':
        
        username=request.POST.get("username")
        if username:
           username=username.lower()
        email=request.POST.get("email")
        if email:
             email=email.lower()
     

        print(email)
        print(username)
        pass1=request.POST.get("password")
        pass2=request.POST.get("confirm-password")

        usernamelog=request.POST.get("usernamelog")
        if usernamelog:
            usernamelog=usernamelog.lower()
      
        passwordlog=request.POST.get("passwordlog")

        user=authenticate(request,username=usernamelog,password=passwordlog)
        
        if user is not None:
            login ( request,user )          
            return redirect('myapp:home')  
        
        if User.objects.filter(email=email).exists():
               messages.error(request,"email is already exist" )
               return render(request, 'loginapp/login.html')
        
        if User.objects.filter(username=username).exists():
               messages.error(request,"username is already exist")
               return render(request, 'loginapp/login.html')
        
        
        if pass1!=pass2:         
          messages.error(request,"both password not match")
          return render(request, 'loginapp/login.html')
        
        if User.objects.filter(username=usernamelog).exists():   
          if user is  None:
             messages.error(request,"Invalid Password or Username" )
             return render(request, 'loginapp/login.html',context={'page': page})
        
        if pass1==pass2:
          user=User.objects.create_user(username,email,pass1)
          user.save()
        #   user.is_active=True
        #   user.save()

        #   current_site=get_current_site(request)
        #   mail_subject="Activate your Account"
        #   message=render_to_string('send_mail_varify/account.html',{
        #       'user':user,
        #       'domain': current_site.domain,
        #       'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        #       'token':default_token_generator.make_token(user)

        #   })
        #   send_mail=EmailMessage(mail_subject,message, to=[email])
        #   send_mail.send()
         
        #   messages.info(request,'activate your account from the mail you provided')
          return redirect('loginapp:login')
         
          login(request,my_user)
          return redirect('myapp:home')    
        
    return render(request, 'loginapp/login.html', context={'page': page})

def activate(request, uidb64, token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=UserModel._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'your account is now active')
        return redirect('loginapp:login')
    else:
         messages.warning(request,'activation link is invalid')
         return redirect('loginapp:login')
    
def userLogout(request):
    logout(request)
    return redirect('loginapp:login')


def userRegister(request):           
  return render(request, 'loginapp/login.html')


def change_passward(request):
     if request.method=='POST':
       print("1 abcdefghijklmnopq")
       form=PasswordChangeForm(request.user, request.POST)
       if form.is_valid():
           user = form.save()
           print("2 abcdefghijklmnopq")
           update_session_auth_hash(request,user)

           messages.success(request,'Password successfully changed')
           return redirect('myapp:home')
     else:
         print("3 abcdefghijklmnopq")
         form=PasswordChangeForm(user=request.user)
     print("4 abcdefghijklmnopq")
     return render(request, 'change_pass/change_pass.html',locals())



def EditUserProfile(request):
    try:
        instance=UserProfile.objects.get(user=request.user)

    except UserProfile.DoesNotExist:
        instance=None

    if request.method=='POST':
        if instance:
            form=UserProfileForm(request.POST, request.FILES, instance=instance)
        else:
            form=UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,'successfully saved your profile')
            return redirect('myapp:home')
    else:
        form=UserProfileForm(instance=instance)

    return render(request, 'loginapp/EditUserProfile.html',locals())



def profile(request):
    
    user=request.user
    
    return render(request, 'loginapp/profile.html',locals())


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'loginapp/profile.html'
    context_object_name='person'

class DeleteUser(SuccessMessageMixin,DeleteView):
    model=User
    template_name='loginapp/user_delete.html'
    success_url=reverse_lazy('myapp:login') 
