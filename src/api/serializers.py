from rest_framework import serializers
from home.models import User
from portfolio.models import Project
from contact.models import Message


class ProjectSerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ["id", "title", "link", "video", "description", "skills"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "message"]

    def save(self, user):
        message = Message(
            name=self.validated_data["name"],
            email=self.validated_data["email"],
            subject=self.validated_data["subject"],
            message=self.validated_data["message"],
            user=user,
        )
        message.save()
        return message
