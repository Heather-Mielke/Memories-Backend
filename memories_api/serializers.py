from rest_framework import serializers
from .models import Post


# serializers.ModelSerializer just tells django to convert sql to JSON
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # tell django which model to use
        # tell django which fields to include
        fields = ('image', 'caption', 'created_date', 'description',)
