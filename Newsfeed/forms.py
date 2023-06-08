from django import forms
from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content','image']
from django.utils.safestring import mark_safe

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','image']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].widget.template_name = 'newsfeed/post_create.html'

# class CustomClearableFileInput(forms.ClearableFileInput):
#     template_name = 'newsfeed/post_create.html'

#     def render(self, name, value, attrs=None, renderer=None):
#         html = super().render(name, value, attrs=attrs)
#         svg = '<svg class="mr-2 cursor-pointer hover:text-gray-700 border rounded-full p-1 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" /></svg>'
#         return mark_safe(svg + html)

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','image']


