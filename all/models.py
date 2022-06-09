from django.db import models
from django.shortcuts import render


class User(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=240)
    img = models.ImageField(upload_to='user-img')
    age = models.DateField(default=14)

    def __str__(self):
        return f'{self.username}'


class Blog(models.Model):
    img = models.ImageField(upload_to='img-blog')
    title = models.CharField(max_length=550)
    started = models.CharField(max_length=5550)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=199)
    short = models.TextField()
    imgs = models.ImageField(upload_to='about_img')
    text = models.TextField()
    happy_clents = models.IntegerField(default=0)
    awords = models.IntegerField(default=0)
    complated_project = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Profile(models.Model):
    img = models.ImageField(upload_to='Img_profile')
    title = models.CharField(max_length=150)
    dic = models.TextField()

    def __str__(self):
        return self.title


class Contect(models.Model):
    name = models.CharField(max_length=169)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField()

    def __str__(self):
        return self.name


