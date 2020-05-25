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

    def validate_content(self, value):
        if len(value) > 1000000:
            raise serializers.ValidationError("This is way too long.")
        return value

    def validate(self, data):
        todolistname = data.get("todolistname", None)
        if todolistname == "":
            todolistname = None
        if todolistname is None:
            raise serializers.ValidationError(
                "todolistname required.")
        return data



class TasklistSerializer(serializers.ModelSerializer,
                         generics.ListAPIView):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'todolistid',
            'taskname',
            'priority',
            'status',
        ]
        read_only_fields = ['todolistid']

    def validate(self, data):
        taskname = data.get("taskname", None)
        if taskname == "":
            taskname = None
        if taskname is None:
            raise serializers.ValidationError(
                "taskname required.")
        return data                         


