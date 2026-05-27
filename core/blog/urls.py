
from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
   path( '', HomeView.as_view(), name='home'),
   path( 'posts/', PostList.as_view(), name='post_list'),
   path( 'posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path( "posts/create/", PostCreate.as_view(), name="post_create"),
   path( "myposts/",MyPosts.as_view(),name="myposts"),
   path( "myposts/update/<int:pk>/",PostUpdate.as_view(),name="post_update"),
   path( "myposts/delete/<int:pk>/",PostDelete.as_view(),name="post_delete"),

]
