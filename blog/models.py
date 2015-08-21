from django.db import models
from django_markdown.models import MarkdownField
from heroku_django.settings import MEDIA_ROOT

# Create your models here.


class TopPost(models.Model):
    topName = models.CharField(max_length=20)
    creattime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topName

class Tag(models.Model):
    tagName = models.CharField(max_length=20)
    creattime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tagName

class Post(models.Model):
    tittle = models.CharField(max_length=50)
    preview = models.CharField(max_length=200)
    body = MarkdownField()
    img = models.ImageField(upload_to="img",default=None,blank=True)
    postime = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)
    topPost = models.ForeignKey(TopPost)
    tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.tittle

