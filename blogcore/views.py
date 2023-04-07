from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blogcore.models import BlogPost
from django.core.paginator import Paginator

def index(request):
    posts = BlogPost.objects.all()[:10]  
    return render(request, 'index.html', context={"posts":posts})

def about(request):
    return render(request, 'about.html', context={})

def post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'post.html', context={"post":post})

def posts(request):
    _posts = BlogPost.objects.all()
    p = Paginator(_posts, 10)
    print(request.GET)
    page_num = request.GET.get('page', 1)
    page = p.get_page(page_num)
    return render(request, 'posts.html', context={"page":page, "p":p})


def contact(request):
    return render(request, 'contact.html', context={})