from django.contrib import admin
from .models import About, Fact, Skill


class AboutInline(admin.StackedInline):
    classes = ["collapse"]
    model = About
    readonly_fields = ("image_tag",)
    extra = 0


class FactInline(admin.TabularInline):
    classes = ["collapse"]
    model = Fact
    extra = 0


class SkillInline(admin.TabularInline):
    classes = ["collapse"]
    model = Skill
    extra = 1
