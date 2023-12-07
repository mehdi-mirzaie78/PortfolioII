from django.contrib import admin
from django.contrib.auth.models import Group
from . import models
from about.admin import AboutInline, FactInline, SkillInline
from resume.admin import SummaryInline, EducationInline, ProfessionalExperienceInline, CVInline

admin.site.unregister(Group)


# ---------------------------------- Home ---------------------------------- #
class LinkInline(admin.TabularInline):
    classes = ['collapse']
    model = models.Link
    extra = 1


class BackgroundInline(admin.TabularInline):
    classes = ['collapse']
    model = models.Background
    readonly_fields = ('image_tag',)
    extra = 1


class TitleInline(admin.TabularInline):
    classes = ['collapse']
    model = models.Title
    extra = 1


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'full_name', 'image_tag', 'is_portfolio']
    inlines = [
        # Home Inlines
        TitleInline, LinkInline, BackgroundInline,
        # About Inlines
        AboutInline, FactInline, SkillInline,
        # Resume Inlines
        SummaryInline, EducationInline, ProfessionalExperienceInline, CVInline,

    ]
    readonly_fields = ('image_tag', 'password', 'last_login', 'date_joined')
    fieldsets = (
        ('General Information', {'fields': ('username', 'email', ('first_name', 'last_name', 'is_portfolio'))}),
        ('Image Information', {
            'fields': (('image_tag', 'image'),),
            'classes': ('collapse',)

        }),
    )
