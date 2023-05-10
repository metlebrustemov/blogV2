from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from blogcore.managers import AdLucemUserManager

class AdLucemUser(AbstractUser):
    USER_TYPES = [
        ("au", "Author"),
        ("rd", "Reader"),
        ("st", "Student"),
    ]
    user_type = models.CharField(max_length=2, choices=USER_TYPES, default="rd")

    username = None
    email = models.EmailField(_("email address"), unique=True)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AdLucemUserManager()

    def __str__(self):
        return self.email

class FollowStatistic(models.Model):
    user = models.OneToOneField(
        AdLucemUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="statistic"
    )
    followers = models.ManyToManyField(AdLucemUser, related_name="followed", blank=True)

    def __str__(self):
        return self.user.email

class Tag(models.Model):
    title = models.CharField(max_length=64,default="")
    slug = models.CharField(max_length=96,default="")
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        instance = super(Tag, self).save(*args, **kwargs)
        
        return instance
    


class BlogPost(models.Model):
    title = models.CharField(max_length=128,default="")
    subtitle = models.CharField(max_length=256,default="")
    description = models.CharField(max_length=512,default="")
    body = RichTextField(default="")
    pub_date = models.DateTimeField('date published', default=timezone.now)
    is_pin = models.BooleanField(default=False, verbose_name="Is Pin")
    is_published = models.BooleanField(default=False, verbose_name="Is Publised")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(AdLucemUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        instance = super(BlogPost, self).save(*args, **kwargs)
        
        return instance
    
class Question(models.Model):
    body = models.CharField(max_length=1536,default="")
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(AdLucemUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.body[:20 if len(self.body)>40 else len(self.body)//2]

class Answer(models.Model):
    body = models.CharField(max_length=1536,default="")
    is_true = models.BooleanField(default=False, verbose_name="Is True")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.body[:20 if len(self.body)>40 else len(self.body)//2]

class Comment(models.Model):
    body = models.CharField(max_length=1536,default="")
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(AdLucemUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.body[:20 if len(self.body)>40 else len(self.body)//2]
    

class Setting(models.Model):
    title = models.CharField(max_length=128,default="Ad Lecum")
    subtitle = models.CharField(max_length=256,default="İşığa doğru")
    about = RichTextField(default="")
    def __str__(self):
        return self.title
    
class SocialAccount(models.Model):
    S_ACCOUNT_TYPES = [
        ("gh", "Github"),
        ("ld", "LinkedIn"),
        ("fb", "FaceBook"),
    ]
    account_type = models.CharField(max_length=2, choices=S_ACCOUNT_TYPES, default="gh")
    name = models.CharField(max_length=40,default="")
    url = models.CharField(max_length=1024,default="")
    user = models.ForeignKey(AdLucemUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
   



