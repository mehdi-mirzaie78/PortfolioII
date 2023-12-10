from django.db import models
from home.models import User


class Summary(models.Model):
    user = models.OneToOneField(User, related_name='summary', on_delete=models.CASCADE)
    about = models.TextField()
    location = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.about[:20]}...'


class Education(models.Model):
    user = models.ForeignKey(User, related_name='educations', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=7, default='Present')
    institution = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.title}'


class ProfessionalExperience(models.Model):
    user = models.ForeignKey(User, related_name='professional_experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=7, default='Present')
    organization = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} - {self.title}'


class ProfessionItem(models.Model):
    experience = models.ForeignKey(ProfessionalExperience, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.experience} - {self.description[:20]}...'


class CV(models.Model):
    user = models.OneToOneField(User, related_name='resume_cv', on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/cv/')

    def __str__(self):
        return f'{self.user} - Resume/CV'
