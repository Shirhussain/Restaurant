from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#third party 
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
        