from rest_framework import serializers
from projectapp.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'url',
            'id',
            'title',
            'url_repo',
            'users',
        )
