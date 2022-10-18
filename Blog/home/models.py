from django.db import models
from datetime import datetime as dt


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.TextField(max_length=250)
    body = models.TextField(max_length=10000)
    date = models.DateField(default=dt.now())

    def __str__(self):
        return self.title
