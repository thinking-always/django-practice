from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "board/home.html", {"posts":posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "board/post_detail.html", {"post":post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "board/post_form.html", {"form":form, "mode":"create"})

def post_udpate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "board/post_form.html", {"form":form, "mode": "update", "post": post})