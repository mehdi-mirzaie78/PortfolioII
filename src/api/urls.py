from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/", views.ProjectView.as_view(), name="projects_view"),
]
