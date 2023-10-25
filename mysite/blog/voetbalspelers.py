from django.conf import settings
from django.db import models
from django.utils import timezone


class Voetbalspelers(models.Model):   
   auteur = models.CharField(max_length=200)
   voetbalspeler = models.CharField(max_length=200)
   voetbalclub = models.CharField(max_length=200)
   created_date = models.DateTimeField(default=timezone.now)
   published_date = models.DateTimeField(blank=True, null=True)

   def publish(self):
       self.published_date = timezone.now()
       self.save()

   def __str__(self):
       return self.title