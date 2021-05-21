from django.urls import path
from . import views



urlpatterns=[
    path("", views.index, name="index"),
    path("posts/", views.authorPosts, name="authorPosts"),
    path("createPost", views.createPost, name="createPost"),
    path("<int:post_id>/editPost", views.editPost, name="editPost"),
    path("<int:post_id>/deletePost", views.deletePost, name="deletePost"),
    path("<int:post_id>/postDetials", views.postDetails, name="postDetails")
]