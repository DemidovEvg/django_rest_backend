
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class UserSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_staff',
            'is_superuser',
            'is_active',
            'email'
        ]


# class AuthorSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=128)
#     birthday_year = serializers.IntegerField()


# class Author:
#     def __init__(self, name, birthday_year):
#         self.name = name
#         self.birthday_year = birthday_year

# from rest_framework.parsers import JSONParser
