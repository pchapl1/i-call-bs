from django.contrib import admin
from .models import Poll, Category


# Register your models here.
admin.site.register([Poll, Category])