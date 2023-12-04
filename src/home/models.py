from django.db import models


class Link(models.Model):
    TITLE_CHOICES = [('li', 'Linkedin'), ('gh', 'Github'), ('tel', 'Telegram'), ('em', 'Email'), ('ig', 'Instagram')]
    title = models.CharField(max_length=255, choices=TITLE_CHOICES, default=TITLE_CHOICES[0][0])
    url = models.URLField(max_length=200)


class About(models.Model):
    pass


class Project(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
