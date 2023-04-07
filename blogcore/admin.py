from django.contrib import admin

from .models import BlogPost, Tag, Setting

@admin.register(BlogPost)
class AdminBlogPost(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'is_published', )
    search_fields = ('title',)
    exclude = ('slug',)

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)
    exclude = ('slug',)

admin.site.register(Setting)
