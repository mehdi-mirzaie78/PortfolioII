from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import User


def index(request):
    user = User.objects.filter(is_portfolio=True).select_related('background', 'about', 'fact').prefetch_related(
        'links', 'titles')
    if user.exists():
        user = user.last()
        links = user.links.all()
        titles = ', '.join(str(title) for title in user.titles.all())
        about = user.about
        fact = user.fact
        skills = user.skills.all()
        summary = user.summary
        educations = user.education.all()
        professional_experiences = user.professional_experiences.prefetch_related('items').all()

        context = {'user': user, 'links': links, 'titles': titles,
                   'about': about, 'fact': fact, 'skills': skills,
                   'summary': summary, 'educations': educations, 'professional_experiences': professional_experiences,
                   }
        return render(request, 'index.html', context)
    return HttpResponse("<h1>No Portfolio Found!</h1>")
