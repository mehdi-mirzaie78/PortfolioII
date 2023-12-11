from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe


class User(AbstractUser):
    image = models.ImageField(upload_to="images/user/", null=True, blank=True)
    is_portfolio = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="150" height="150" />')
        return mark_safe(f'<img src="#" width="150" height="150" />')

    def __str__(self):
        return self.full_name


class Title(models.Model):
    user = models.ForeignKey(User, related_name="titles", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    show_in_about = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Link(models.Model):
    class LinkChoices(models.TextChoices):
        LINKEDIN = "li", "Linkedin"
        GITHUB = "gh", "Github"
        TELEGRAM = "tel", "Telegram"
        EMAIL = "em", "Email"
        INSTAGRAM = "ig", "Instagram"

    user = models.ForeignKey(User, related_name="links", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, choices=LinkChoices.choices, unique=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.url}"


class Background(models.Model):
    user = models.OneToOneField(
        User, related_name="background", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="images/background/", default="images/background/default.jpg"
    )

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="300" height="200" />')

    def __str__(self):
        return f"{self.user} - {self.image}"
