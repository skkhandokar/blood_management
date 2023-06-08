from django.urls import path
from .views import post_create, post_list,PostDetailView,post_update_view,post_delete,LikeView,cmntLikeView
from .views import update_comment,CommentDeleteView,otherprofile,addcomment,notification,ReadNotification

app_name='newsfeed'
urlpatterns = [
    path('post-create/', post_create, name='post_create'),
    path('newsfeed/', post_list, name='post_list'),
    path('addcomment/', addcomment, name='addcomment'),
    path('postdetail/<int:pk>', PostDetailView, name='post_detail_view'),
    path('edit/<int:pk>', post_update_view.as_view(), name='post_update_view'),
    path('comment-edit/<int:pk>/<int:pk2>',update_comment.as_view() , name='comment_update_view'),
    path('delete/<int:pk>', post_delete.as_view(), name='post_delete'),
    path('comment-delete/<int:pk>/<int:pk1>', CommentDeleteView.as_view(), name='post_delete'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('cmntlike/<int:pk>/<int:pk2>',cmntLikeView, name='cmntlike_post'),

    path('profile/<str:username>', otherprofile, name='otherprofile'),
    path('notification/', notification, name='notification'),
     path('read-notification/', ReadNotification, name='read-notification'),

]