from django.shortcuts import render
from django.http import HttpResponse
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

        context = {'user': user, 'links': links, 'titles': titles, 'about': about, 'fact': fact, 'skills': skills}
        return render(request, 'index.html', context)
    return HttpResponse("<h1>No Portfolio Found!</h1>")
