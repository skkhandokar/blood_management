from django.db import models
from datetime import datetime,date

from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=False)
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=False)
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
    

class Bloods_Group(models.Model):
    blood = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.blood
    
    # class Meta:
    #     #jeta pore add hobe seta age dekhabe
    #     ordering=['-blood',]
        
    



class Donors_in_Site(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=124,default='username',blank=False)
    phone=models.CharField(max_length=14,null=True,blank=True) 
 
    blood = models.CharField(max_length=124,null=True,blank=False)   
    blood_donate_times=models.IntegerField(default=0,null=True,blank=True)
  
    Last_Donate=   models.CharField(max_length=11,null=True)
    image= models.ImageField(upload_to='donors_in_site',null=True,blank=True)
    country = models.CharField(max_length=124,null=True,blank=False)
   
    state = models.CharField(max_length=124,null=True,blank=False)
    
    district= models.CharField(max_length=124,null=True,blank=False)
    slug = models.SlugField(unique=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.blood
    
    def get_donor_url(self):
        return reverse('myapp:donor_details',kwargs={'slug':self.slug}) #je url diye jabe tar name
       
       #slug is filter.slug jate product name e save hoy er jonno function
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        return super().save(*args, **kwargs)
    

    age = models.IntegerField(null=True,blank=True)
    
    def getage(self):
        my_date = self.dob
        b_date = datetime.strptime(my_date, '%d/%m/%Y')
        age=int((datetime.today() - b_date).days/365)    
        age=age
        return age 

        #   today = date.today()
        # age = today.year - self.birthdate
        # if today.month < self.birthdate.month or today.month == self.birthdate.month and today.day < self.birthdate.day:
        #   age -= 1

    def month(self):

           my_date = self.dob
           mymonthmonth=int(my_date[3:5])
           todaymonth=int(date.today().strftime("%m"))
           month=abs (todaymonth-mymonthmonth)
           month=month
           return month
    
    def day(self):
           my_date = self.dob
           myday=int(my_date[:2])
           today=int(date.today().strftime("%d"))    
           day=abs (today-myday)
           return day

# Create your models here.

class Contact_us(models.Model):

    sender_name=models.CharField(max_length=100)
    from_email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_email