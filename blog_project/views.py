from django.shortcuts import render
from posts.models import Posts


def home(request):
    post = Posts.objects.all()
    return render(request, 'home.html', {'data': post})
