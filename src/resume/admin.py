from django.contrib import admin
from .models import Summary, Education, ProfessionalExperience, CV, ProfessionItem


class SummaryInline(admin.TabularInline):
    classes = ['collapse']
    model = Summary
    extra = 0


class EducationInline(admin.StackedInline):
    classes = ['collapse']
    model = Education
    extra = 0


class ProfessionItemInline(admin.TabularInline):
    classes = ['collapse']
    model = ProfessionItem
    extra = 0


class ProfessionalExperienceInline(admin.TabularInline):
    classes = ['collapse']
    model = ProfessionalExperience
    extra = 0
    show_change_link = True


@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    inlines = [ProfessionItemInline]


class CVInline(admin.TabularInline):
    classes = ['collapse']
    model = CV
    extra = 0
