from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    image = models.TextField(null=True, blank=True)
    caption = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
