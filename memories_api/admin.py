from django.contrib import admin
from .models import Memory, Post_Comment, Post_Favorite
# Register your models here.
admin.site.register(Memory)
admin.site.register(Post_Comment)
admin.site.register(Post_Favorite)
