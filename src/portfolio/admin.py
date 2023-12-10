from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('video_tag',)
    list_display = ('title', 'user', 'link', 'video')
    search_fields = ('title', 'link', 'skills__title')
    filter_horizontal = ('skills',)
    list_filter = ('skills',)


class ProjectInline(admin.StackedInline):
    filter_horizontal = ('skills',)
    classes = ('collapse',)
    model = Project
    extra = 0
