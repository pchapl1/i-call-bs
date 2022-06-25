import re
from django import forms
from django.forms import ModelForm
from .models import Poll


class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'

        widgets = {
            'title':forms.TextInput(attrs={'class' : 'form-control' }),
            'body' : forms.Textarea(attrs={'class' : 'form-control' }),
            'author' : forms.HiddenInput(attrs={'class' : 'form-control form-select' }),
            'likes' : forms.HiddenInput(attrs={'class' : 'form-control form-select' }),
            'dislikes' : forms.HiddenInput(attrs={'class' : 'form-control form-select' }),
            'total_votes' : forms.HiddenInput(attrs={'class' : 'form-control form-select' }),

        }