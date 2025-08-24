from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_create, name="post_create"),
    path("post/<int:pk>/edit/", views.post_udpate, name="post_update"),
]