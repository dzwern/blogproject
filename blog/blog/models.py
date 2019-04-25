from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.urls import reverse
#分类
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

#标签
class Tag(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

#文章
class Post(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=255,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pk':self.pk})


