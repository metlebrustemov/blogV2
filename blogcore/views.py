from django.shortcuts import render

from blogcore.models import BlogPost

def index(request):
    posts = BlogPost.objects.all()[:10]  
    return render(request, 'index.html', context={"posts":posts})

def about(request):
    return render(request, 'about.html', context={})

def post(request):
    return render(request, 'post.html', context={})

def posts(request):
    return render(request, 'posts.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})