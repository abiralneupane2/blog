

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=96)
    last_name = models.CharField(max_length=96)




class Author(models.Model):
    user = models.OneToOneField("blog.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Blog(models.Model):
    author = models.ForeignKey("blog.Author", on_delete=models.CASCADE)
    text = models.TextField(default="")
    title = models.CharField(max_length=96)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.title}"


class BlogImages(models.Model):
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE)
    file = models.FileField(upload_to="blog_files/")


class Comment(models.Model):
    text = models.TextField()
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
