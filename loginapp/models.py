from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from PIL import Image 
from django.contrib.auth.models import AbstractUser



 
    
   

class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    )


    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100,null=True,blank=True)
    birth_date=models.DateField(blank=True)
    gender=models.CharField(max_length=50,choices =GENRE_CHOICES ,blank=True)
    address=models.CharField(max_length=150,blank=True)
    permanant_address=models.CharField(max_length=150,null=True,blank=True)
    nationality=models.CharField(max_length=100,blank=True)
    religion=models.CharField(max_length=100,blank=True)
    biodata=models.TextField(blank=True)
    profession=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(default='demo.png',upload_to='user_profile',blank=True)
    slug = models.SlugField(default='username')


    def get_user_url(self):
        
        return reverse('loginapp:user_profile',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

 
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
