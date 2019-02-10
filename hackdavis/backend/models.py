from django.db import models

# Create your models here.
class Event(models.Model):
    image_link = models.CharField(max_length=150)
    event_address = models.CharField(max_length=300)
    importance_rank = models.IntegerField()
    event_description = models.CharField(max_length=300)