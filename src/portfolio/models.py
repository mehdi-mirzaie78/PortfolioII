from django.db import models
from django.utils.html import mark_safe
from home.models import User
from about.models import Skill


class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, related_name="projects", blank=True)

    def __str__(self):
        return f"{self.title} - {self.link}"

    def video_tag(self):
        return mark_safe(
            f"""
        <video width="600" height="400" controls><source src="{self.video.url}" type="video/mp4"></video>
        """
        )
