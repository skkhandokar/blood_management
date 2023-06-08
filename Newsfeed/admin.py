from django.contrib import admin
from .models import Post,Comment
from django.utils.html import format_html
from django.utils import timezone
# Register your models here.
admin.site.site_header='SKKHANDOKAR Admin Panel'
admin.site.site_title= 'SKKHANDOKAR Admin Panel'
admin.site.index_title= ''
class CommentInline(admin.TabularInline):
   model=Comment

class PostAdmin(admin.ModelAdmin):
 list_display=('author','title',"title_html_display",'content',"views_count","created_at")
 list_filter=('author','title','content')
 inlines=[
  CommentInline, 
 ]
 def title_html_display(self,obj):
  return format_html(
   f'<span style="font-size:20px; color:blue; ">{obj.title} </span>'
  )
admin.site.register(Post,PostAdmin)
admin.site.register(Comment )
