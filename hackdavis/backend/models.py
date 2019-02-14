from django.db import models

# Create your models here.
class Event(models.Model):
    event_description = models.CharField(max_length=50)