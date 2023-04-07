from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blogcore.models import BlogPost

def index(request):
    posts = BlogPost.objects.all()[:10]  
    return render(request, 'index.html', context={"posts":posts})

def about(request):
    return render(request, 'about.html', context={})

def post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'post.html', context={"post":post})

def posts(request):
    return render(request, 'posts.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})