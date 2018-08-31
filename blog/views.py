from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    posts = Post.published.all()
    return render(request, 'blog/index.html', context={'posts': posts})
