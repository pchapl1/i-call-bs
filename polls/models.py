from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    type = models.CharField(max_length=55)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('home')

class Poll(models.Model):
    body = models.TextField(max_length=5000)
    bullshitter = models.CharField(max_length=75)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='categories')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
