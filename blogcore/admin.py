from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blogcore.forms import AdLucemUserChangeForm, AdLucemUserCreationForm

from blogcore.models import AdLucemUser, BlogPost, Tag, Setting

class AdLucemUserAdmin(UserAdmin):
    add_form = AdLucemUserCreationForm
    form = AdLucemUserChangeForm
    model = AdLucemUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(AdLucemUser, AdLucemUserAdmin)

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
