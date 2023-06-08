from tkinter import Image
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image=models.FileField(null=True,blank=True,upload_to='post_images')
    # images = MultiSelectField(choices=[('image1', 'Image 1'), ('image2', 'Image 2')])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.ManyToManyField(User ,related_name='post_views')
    views_count = models.IntegerField(default=0)
    likes = models.ManyToManyField(User ,related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs={'pk': self.pk})
    
    def total_views(self):
         return self.views.count()
   
    
    def total_likes(self):
         return self.likes.count()

    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs) 

class Comment(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='comment_images')
    cmnt_likes = models.ManyToManyField(User ,related_name='comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    time       = models.TimeField(auto_now_add=True,null=True)
    p_time=datetime.now()

 

    def total_likes(self):
         return self.cmnt_likes.count()
    
    def __str__(self):
        return self.author.username +": " +self.content[0:15]
    
    def dif_days(self):
            time_since_posted = datetime.now() - self.created_at
            return time_since_posted

   
