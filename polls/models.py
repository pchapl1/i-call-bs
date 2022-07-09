from django.db import models
from django.urls import reverse

class Poll(models.Model):
    title = models.CharField(max_length=245)
    body = models.TextField(max_length=5000)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


