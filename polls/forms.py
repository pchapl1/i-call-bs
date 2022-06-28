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
            'bullshitter' : forms.TextInput(attrs={'class' : 'form-control' }),
            'likes' : forms.HiddenInput(attrs={'class' : 'form-control' }),
            'dislikes' : forms.HiddenInput(attrs={'class' : 'form-control' }),
            'total_votes' : forms.HiddenInput(attrs={'class' : 'form-control' }),
            'created_by' : forms.HiddenInput(attrs={'class' : 'form-control' }),
        }