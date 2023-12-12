from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/", views.ProjectView.as_view(), name="projects_view"),
    path("send-message/", views.SendMessageView.as_view(), name="message_view"),
]
