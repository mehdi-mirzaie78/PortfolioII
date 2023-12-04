from django.shortcuts import render
from .models import User


def index(request):
    user = User.objects.filter(is_active=True).select_related('background').prefetch_related('links', 'titles').first()
    links = user.links.all()
    titles = ', '.join(str(title) for title in user.titles.all())
    return render(request, 'index.html', {'user': user, 'links': links, 'titles': titles})
