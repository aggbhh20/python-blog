from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
class Itemblogposts(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    idNum = models.IntegerField()