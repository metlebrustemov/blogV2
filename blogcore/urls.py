from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('contact', views.contact, name='contact'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('tag/<slug:slug>/', views.tag, name='tag'),
]
