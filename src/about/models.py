from django.db import models
from home.models import User
from django.utils.html import mark_safe
from datetime import date


class About(models.Model):
    user = models.OneToOneField(User, related_name='about', on_delete=models.CASCADE)
    head_paragraph = models.TextField()
    image = models.ImageField(upload_to='images/about/', null=True, blank=True)
    birth_date = models.DateField()
    website = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)

    class FreelanceChoices(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        UNAVAILABLE = 'unavailable', 'Unavailable'

    freelance = models.CharField(max_length=20, choices=FreelanceChoices.choices, default=FreelanceChoices.UNAVAILABLE)
    main_paragraph = models.TextField()

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year

    @property
    def title(self):
        return self.user.titles.filter(show_in_about=True).last()

    @property
    def email(self):
        return self.user.links.get(title='em').url

    def __str__(self):
        return f'{self.user} - {self.title}'

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="300" height="200" />')


class Fact(models.Model):
    user = models.OneToOneField(User, related_name='fact', on_delete=models.CASCADE)
    text = models.TextField()
    happy_clients = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    hours_of_support = models.PositiveIntegerField()
    hard_workers = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} - {self.text}'


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    percent = models.PositiveIntegerField(default=90)

    def __str__(self):
        return self.title
