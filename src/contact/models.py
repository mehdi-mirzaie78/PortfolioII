from django.db import models


class Contact(models.Model):
    user = models.OneToOneField(
        "home.User", related_name="contact", on_delete=models.CASCADE
    )
    main_paragraph = models.TextField(null=True, blank=True)
    google_map = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.main_paragraph if self.main_paragraph else ''}"


class Message(models.Model):
    user = models.ForeignKey(
        "home.User", related_name="messages", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.name} - {self.subject}"
