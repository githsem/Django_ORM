from django.db import models
from django.utils import timezone

# Create your models here.

class BaseItem(models.model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)