from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count', 'created_at')
    list_filter = ('is_published', 'created_at')
    list_editable = ('is_published',)
