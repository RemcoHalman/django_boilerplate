from django.contrib import admin
from django.contrib.auth.models import Group
from decouple import config, Csv

from .models import Page, Testimonial, BlogPost, Project

admin.site.unregister(Group)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "id","title", "slug", "background_image",
        )
    readonly_fields = ('id',)

    def get_queryset(self, request):
        queryset = super(PageAdmin, self).get_queryset(request)
        queryset = queryset.order_by('id')
        return queryset

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "content", "writer", "verification_url", "writer_profile_image",
        )

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title", "slug", "background_image", "author",
        )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title", "slug", "project_image", "author",
        )
