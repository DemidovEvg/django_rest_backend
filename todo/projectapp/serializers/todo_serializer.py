from rest_framework import serializers
from projectapp.models import Todo
from django.contrib.auth import get_user_model


User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'project',
            'project_id',
            'text',
            'created_at',
            'updated_at',
            'author',
            'author_id',
            'is_active'
        )
