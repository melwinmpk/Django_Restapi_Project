from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from todolistcore.models import TodoList, Tasks
from .serializers import TodolistSerializer
import json


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class CreateTodoAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        todoListName = data.get('todolistname')
        subjaectobj = TodoList(todolistname=todoListName,
                               user=self.request.user)
        subjaectobj.save()
        return Response({"detail": "A new ToDo list got created  "}, status=201)


class ListTodoAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['todolistname'] for entry in qs.values()]
        return Response({"success": "list of data  ", "data": list_result}, status=201)
        # return Response({"detail": "A new ToDo list got created  "}, status=201)

class TodoListSerializerAPIView(mixins.CreateModelMixin,
                    generics.ListAPIView):
    # permission_classes = []
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class   = TodolistSerializer
    passed_id          = None

    def get_queryset(self):
        request = self.request
        qs = TodoList.objects.filter(
            user=self.request.user)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get(self, request, format=None):
        qs = TodoList.objects.filter(
            user=self.request.user)
        serializer_class = TodolistSerializer(qs, many=True)
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateTaskAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        data = request.data
        id = data.get('id')
        taskname = data.get('taskname')
        priority = data.get('priority')
        '''
        questionobj = Questions(
            SubjectId       = SubjectDefinition.objects.get(SubjectId=self.subjectid),
            Question        = self.Question,
            Options         = self.options,
            QuestionTypeId  = QuestionDefinition.objects.get(QuestionTypeId=self.questiontype),
            Ans             = self.Ans)
        questionobj.save()
        '''
        subjaectobj = Tasks(
            todolistid=TodoList.objects.get(id=id),
            taskname=taskname,
            priority=priority
            )
        subjaectobj.save()
        return Response({"detail": "A new Task Got Created  "}, status=201)
