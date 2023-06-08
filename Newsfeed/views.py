from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView,ListView,DeleteView
from django.views.decorators.cache import never_cache
from .templatetags import tag
from notifications.signals import notify
import PIL.Image 
def post_create(request):

    if request.method == 'POST':
        
        form = PostForm (request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if 'image' in request.FILES:
                   post.image = request.FILES['image']
                   post.save()
            
            return redirect('newsfeed:post_list')
    else:
        form = PostForm()
    posts = Post.objects.order_by('?')
    
    return render(request, 'newsfeed/post_create.html',locals())

@login_required
def post_list(request):
    posts = Post.objects.order_by('?')
    return render(request, 'newsfeed/post_list.html', {'posts': posts})

class post_detail_view(DetailView):
    model=Post
    template_name='newsfeed/post_detail_view.html'
 
    context='post'

from django.views.generic.edit import FormMixin

# class PostDetailView(FormMixin, DetailView):
#     model = Post
#     form_class = CommentForm
#     template_name = 'newsfeed/post_detail_view.html'

#     def get_success_url(self):
#         return reverse('newsfeed:post_detail_view', kwargs={'pk': self.object.pk})

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = self.object
#             if 'image' in request.FILES:
#                 comment.image = request.FILES['image']
#             comment.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def get_context_data(self, *args,**kwargs):
#         context = super().get_context_data(**kwargs)
#         self.object = self.get_object()
       
       
        # if self.request.user.is_authenticated:
        #     self.object.views.add(self.request.user)
        # self.object.views_count += 1
        # self.object.save()
#         context['comments'] = self.object.comments.order_by('-created_at')
#         stuff=get_object_or_404(Post,id=self.kwargs['pk'])
#         total_likes=stuff.total_likes()
#         context['ln'] = len(context['comments'])
#         context['total_likes'] = total_likes
#         return context

def PostDetailView(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments=Comment.objects.filter(post=post.id,parent=None).order_by('-created_at')
    replies=Comment.objects.filter(post=post.id).exclude(parent=None ).order_by('-created_at')
    dicReply={}
    for reply in replies:
        if reply.parent.id not in dicReply.keys():
            dicReply[reply.parent.id]=[reply]
        else:
            dicReply[reply.parent.id].append(reply)
    # comments = post.comments/addcomment/"
    total_likes = post.total_likes()
    cln = len(comments)
    rln = len(replies)
    ln=cln+rln

    if request.method == 'POST':
        form = CommentForm(request.POST)
        parentid=request.POST['parentid']
        content=request.POST['content']
        postid=request.POST['postid']
        post=Post.objects.get(id=postid)
        if parentid:
                parent=Comment.objects.get(id=parentid)
            
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.parent=parent
                comment.content=content
                if 'image' in request.FILES:
                    comment.image = request.FILES['image']
                comment.save()
            

        else:
          if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            if 'image' in request.FILES:
                comment.image = request.FILES['image']
            comment.save()
      
        return redirect('newsfeed:post_detail_view', pk=post.pk)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'total_likes': total_likes,
        'ln': ln,
        'form': form,
    }
    if request.user.is_authenticated:
        post.views.add(request.user)
    
    post.views_count += 1
    post.save()
    return render(request, 'newsfeed/post_detail_view.html', locals())

def addcomment(request):
   
     if request.method == 'POST':
        form = CommentForm(request.POST)
        parentid=request.POST['parentid']
        content=request.POST['content']
        postid=request.POST['postid']
        post=Post.objects.get(id=postid)
        
        if parentid:
       
                parent=Comment.objects.get(id=parentid)
                print(parent.author)
                newcom=Comment(content=content,author=request.user,post=post,parent=parent)
                newcom.save()
                if 'image' in request.FILES:
                    newcom.image = request.FILES['image']
                    
                
                newcom.save()
                
                if request.user != parent.author:

                    if parent.author ==post.author :
                         notify.send(recipient=parent.author,sender=request.user,verb=" "  + f''' <a href="/postdetail/{post.pk}"> replied your post </a>''',target=post)
                    else:
                         notify.send(recipient=parent.author,sender=request.user,verb=" "  + f''' <a href="/postdetail/{post.pk}"> replied  {post.author}'s post </a>''',target=post)
       
        else:
          
        #   if form.is_valid():
        #     comment = form.save(commit=False)
        #     comment.author = request.user
        #     comment.post = post

            newcom=Comment(content=content,author=request.user,post=post)
            newcom.save()
            if 'image' in request.FILES:
                newcom.image = request.FILES['image']

            newcom.save()
            if request.user != post.author:
             
                     notify.send(recipient=post.author,sender=request.user,verb=" "  + f''' <a href="/postdetail/{post.pk}"> commented your post </a>''',target=post)
                 
           
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return redirect('newsfeed:post_detail_view', pk=post.pk)

class post_update_view(UpdateView):
    model = Post
    fields = ['title', 'content','image'] # Add fields that you want to update here
    template_name= 'newsfeed/post_create.html'

    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('newsfeed:post_detail_view', kwargs={'pk':id})
    
class update_comment(UpdateView):
    model = Comment
    fields = [ 'content','image'] # Add fields that you want to update here
    template_name= 'newsfeed/comment_update.html'

    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('newsfeed:post_detail_view', kwargs={'pk': self.kwargs['pk2']})



 
class post_delete(DeleteView):
      model = Post
      template_name='newsfeed/post_delete.html'
      success_url=reverse_lazy('newsfeed:post_create')

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'newsfeed/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('newsfeed:post_detail_view', kwargs={'pk': self.kwargs['pk1']})

def LikeView(request,pk):
    post = get_object_or_404(Post, pk=pk)
  
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        return HttpResponseRedirect(reverse('newsfeed:post_detail_view', args=[str(pk)]) )
        
    else:
        post.likes.add(request.user)

        if request.user != post.author:
            notify.send(recipient=post.author,sender=request.user,verb=" "  + f''' <a href="/postdetail/{post.pk}">  has liked your post  </a>''')
       
        return HttpResponseRedirect(reverse('newsfeed:post_detail_view', args=[str(pk)]) )
    
def cmntLikeView(request,pk,pk2):
   
    post = get_object_or_404(Comment, pk=pk)
    if request.user in post.cmnt_likes.all():
        post.cmnt_likes.remove(request.user)
        return HttpResponseRedirect(reverse('newsfeed:post_detail_view', args=[str(pk2)]))
        
    else:

        post.cmnt_likes.add(request.user)
        if request.user != post.author:
            notify.send(recipient=post.author,sender=request.user,verb=" "  + f''' <a href="/postdetail/{post.pk}">  has liked your comment  </a>''')
       
        return HttpResponseRedirect(reverse('newsfeed:post_detail_view', args=[str(pk2)]))

 


from django.contrib.auth.models import User
def otherprofile(request,username):
    user=User.objects.get(username=username)
    return render (request,'loginapp/profile.html',locals())


        
from notifications.models import Notification
def notification(request):
   
    return render (request, 'newsfeed/notification.html')


def ReadNotification(request):
    notifications = Notification.objects.filter(recipient=request.user)
    for notification in notifications:
            notification.mark_as_read()
    return render (request, 'newsfeed/notification.html')