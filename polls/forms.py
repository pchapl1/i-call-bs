import re
from django import forms
from django.forms import ModelForm
from .models import Poll


class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'

        widgets = {
            'title':forms.TextInput(attrs={'class' : 'form-control' ,"placeholder":"Title"}),
            'body' : forms.Textarea(attrs={'class' : 'form-control',"placeholder":"Body" }),
            # 'author' : forms.HiddenInput(attrs={'class' : 'form-control form-select',"placeholder":"Author" }),
            'likes' : forms.HiddenInput(attrs={'class' : 'form-control form-select',"placeholder":"Likes" }),
            'dislikes' : forms.HiddenInput(attrs={'class' : 'form-control form-select',"placeholder":"Dislikes" }),
            'total_votes' : forms.HiddenInput(attrs={'class' : 'form-control form-select',"placeholder":"Total Votes" }),

        }