from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=70, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True)
    completed = models.BooleanField(default=False)