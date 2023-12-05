from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    user = User.objects.filter(is_portfolio=True).select_related('background').prefetch_related('links', 'titles')
    if user.exists():
        user = user.last()
        links = user.links.all()
        titles = ', '.join(str(title) for title in user.titles.all())
        return render(request, 'index.html', {'user': user, 'links': links, 'titles': titles})
    return HttpResponse("<h1>No Portfolio Found!</h1>")
