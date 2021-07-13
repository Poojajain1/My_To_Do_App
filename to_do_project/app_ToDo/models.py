from django.db import models

# Create your models here.
class ToDOItem(models.Model):
    content=models.TextField()