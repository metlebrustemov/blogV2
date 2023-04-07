from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField


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
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        instance = super(BlogPost, self).save(*args, **kwargs)
        
        return instance

class Setting(models.Model):
    title = models.CharField(max_length=128,default="")
    subtitle = models.CharField(max_length=256,default="")
    about = RichTextField(default="")
    def __str__(self):
        return self.title
    
   



