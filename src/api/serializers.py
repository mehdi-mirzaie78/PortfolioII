from rest_framework import serializers
from portfolio.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ["id", "title", "link", "video", "description", "skills"]
