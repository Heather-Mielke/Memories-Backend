from django.db import models


# Create your models here.

class Post(models.Model):
    image = models.TextField(null=True, blank=True)
    caption = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
