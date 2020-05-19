import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework import generics, mixins, permissions
from todolistcore.models import TodoList, Tasks
# expire_delta = api_settings.REFRESH_TOKEN_LIFETIME


class TodolistSerializer(serializers.ModelSerializer, 
                         generics.ListAPIView):
    class Meta:
        model = TodoList
        fields = [
            'id',
            'todolistname',
            'user'
        ]
        read_only_fields = ['user']


class TasksSerializer(serializers.ModelSerializer):
    pass

