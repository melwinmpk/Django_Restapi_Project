from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from todolistcore.models import TodoList, Tasks
from .serializers import TodolistSerializer, TasklistSerializer
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
        data     = request.data
        todolistid = data.get('todolistid')
        taskname = data.get('taskname')
        priority = data.get('priority')
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)

        subjaectobj = Tasks(
            todolistid=TodoList.objects.get(id=todolistid),
            taskname   = taskname,
            priority   = priority
            )
        subjaectobj.save()
        return Response({"detail": "A new Task Got Created  "}, status=201)


class ListTasksAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        todolistid = data.get('todolistid')
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        qs = Tasks.objects.filter(
            todolistid=todolistid)
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)

        list_result = [entry for entry in qs.values()]
        return Response({"success": "list of data  ", "data": list_result}, status=201)


class TaskListSerializerAPIView(mixins.CreateModelMixin,
                                generics.ListAPIView):
    serializer_class = TasklistSerializer
    passed_id = None

    # def get_queryset(self):
    #     request = self.request
    #     qs = TodoList.objects.filter(
    #         user=self.request.user,)
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs

    def get(self, request, format=None):
        todolistid = request.data.get("todolistid", None)
        qs = TodoList.objects.filter(
            user=self.request.user)
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)
        qs = Tasks.objects.filter(
            todolistid=todolistid)
        serializer_class = TasklistSerializer(qs, many=True)
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        todolistid = request.data.get("todolistid", None)
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(todolistid=TodoList.objects.get(
            id=self.request.data.get("todolistid")))

class UpdateTaskAPIView(APIView):
    def put(self, request, *args, **kwargs):
        todolistid = request.data.get("todolistid", None)
        taskid = request.data.get("taskid", None)
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)
        Tasks.objects.filter(id=taskid).update(status=True)
        return Response({"detail": "A Task Got Updated  "}, status=201)


class DeleteTaskAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        todolistid = request.data.get("todolistid", None)
        taskid = request.data.get("taskid", None)
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)
        Tasks.objects.filter(id=taskid).delete()
        return Response({"detail": "A Task Got Deleted  "}, status=201)
        

class TaskSerializerAPIView(mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            generics.RetrieveAPIView):
    serializer_class = TasklistSerializer
    lookup_field = 'id'

    def get_object(self, *args, **kwargs):  # slug method for handeling the
        kwargs = self.kwargs
        kw_id = self.request.data.get('id')
        qs = Tasks.objects.get(id=kw_id)
        return qs

    def put(self, request, *args, **kwargs):
        print(request.data)
        todolistid = request.data.get("todolistid", None)
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        todolistid = request.data.get("todolistid", None)
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)
        return self.update(request, *args, **kwargs)                            
    
    def delete(self, request, *args, **kwargs):
        todolistid = request.data.get("todolistid", None)
        qs = TodoList.objects.filter(
            user=self.request.user).values('todolistname')
        list_result = [entry['id'] for entry in qs.values()]
        if int(todolistid) not in list_result:
            return Response({"detail": "todolistid not found for this user  "}, status=404)
        return self.destroy(request, *args, **kwargs)

                                


