from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView, PostUpdateView, CommentCreateView, PostDeleteView
urlpatterns = [
    path("", PostListView.as_view() , name="home"),
    path("post/<int:pk>/", PostDetailView.as_view() , name="post_detail"),
    path("post/new/", PostCreateView.as_view() , name="post_create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view() , name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view() , name="post_delete"),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment_create"),
]