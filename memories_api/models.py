
from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)

class Memory(models.Model):
    creator = models.ForeignKey('auth.user', related_name="memories",
                                on_delete=models.CASCADE, null=True)
    image = models.TextField(null=True, blank=True)
    caption = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

class Post_Favorite(models.Model):
    user = models.ForeignKey('auth.user', related_name="post_favorites", on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, related_name="favorites", on_delete=models.CASCADE)
    like = models.BooleanField()

class Post_Comment(models.Model):
    user = models.ForeignKey('auth.user', related_name="post_comments", on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
