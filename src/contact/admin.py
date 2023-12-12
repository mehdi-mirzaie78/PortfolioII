from django.contrib import admin
from .models import Contact, Message


class ContactInline(admin.StackedInline):
    classes = ["collapse"]
    model = Contact
    extra = 0


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "email", "subject")
    list_filter = ("user", "name", "email", "subject")
    search_fields = ("user", "name", "email", "subject")
