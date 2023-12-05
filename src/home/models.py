from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe


class User(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_portfolio = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="150" height="150" />')
        return mark_safe(f'<img src="#" width="150" height="150" />')

    def __str__(self):
        return self.full_name


class Title(models.Model):
    user = models.ForeignKey(User, related_name='titles', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Link(models.Model):
    user = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    TITLE_CHOICES = [('li', 'Linkedin'), ('gh', 'Github'), ('tel', 'Telegram'), ('em', 'Email'), ('ig', 'Instagram')]
    title = models.CharField(max_length=255, choices=TITLE_CHOICES, unique=True)
    url = models.URLField(max_length=255)

    def __str__(self):
        return f'{self.title} - {self.url}'


class Background(models.Model):
    user = models.OneToOneField(User, related_name='background', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/background/', default='images/background/default.jpg')

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="300" height="200" />')

    def __str__(self):
        return f'{self.user} - {self.image}'
