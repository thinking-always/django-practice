from django.shortcuts import get_object_or_404, render
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = "board/home.html"
    paginate_by = 10
    ordering = "-created_at"
    context_object_name = "posts"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "board/post_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comments"] = self.object.comments.all()
        ctx["form"] = CommentForm()
        return ctx
    
    
class PostCreateView(CreateView):
    model = Post
    template_name = "board/post_form.html"
    form_class = PostForm
    
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = "board/post_form.html"
    form_class = PostForm
    context_object_name = "post"
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = "board/post_delete.html"
    success_url = reverse_lazy("home")
    
  
    
class CommentCreateView(CreateView):
    model = Comment
    template_name = "board/comment_form.html"
    form_class = CommentForm
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        return super().form_valid(form)
    
    def form_invalid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        comments = post.comments.all().order_by("-created_at")
        return render(self.request, "board/post_detail.html", {
            "post":post,
            "comments": comments,
            "form": form,
        }, status=400)
    
   
    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.kwargs["pk"]})