from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.db.models import Count
from collections import Counter

class Category(models.Model):
    type = models.CharField(max_length=55)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('home')





class Poll(models.Model):
    body = models.TextField(max_length=5000)
    bullshitter = models.CharField(max_length=75)
    total_votes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='polls')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    bs_votes = models.IntegerField(default=0)
    true_votes = models.IntegerField(default=0)


    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('home')

    def bs_count(self):
        count = 0
        for x in self.votes.all():
            if x.is_bs == False:
                count +=1
        return count

    def truth_count(self):
        count = 0
        for x in self.votes.all():
            if x.is_bs == True:
                count +=1
        return count

    def get_total_votes(self):
        votes_today = self.votes.all()
        count = 0
        for x in votes_today:
            if x.date_created == date.today():
                count +=1
        return count

class Vote(models.Model):
    is_bs = models.BooleanField(blank=True, null=True) # a false vote means its bullshit, true means true
    voted_on_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='votes')
    poll = models.ForeignKey(Poll, blank=True, null=True, on_delete=models.CASCADE, related_name='votes')
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    


