from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title", "body")
    
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ("content","post","created_at")
    search_fields = ("content","created_at")

