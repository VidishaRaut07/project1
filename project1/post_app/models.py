from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_by = models.CharField(max_length=40)
    