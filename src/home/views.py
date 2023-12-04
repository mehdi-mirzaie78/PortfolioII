from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    [print(project.video.url) for project in projects]
    return render(request, 'index.html', {'projects': projects})
