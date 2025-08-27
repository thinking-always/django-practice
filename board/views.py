from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def home(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "board/home.html", {"posts":posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, "board/post_detail.html", {
        "post":post,
        "comments":comments,
        "form":form
         })

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

def comment(request, pk):
    comments = Comment.objects.order_by("-created_at")
    return render(request, "board/post_detail.html", {"comments":comments})
