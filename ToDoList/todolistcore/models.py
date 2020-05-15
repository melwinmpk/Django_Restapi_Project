from django.db import models
from django.conf import settings
# Create your models here.
'''
TodoList
-> id (Primary)
-> UserId (foreignkey)
-> TodoListName

Tasks
-> TodoList id (foreign key)
-> Taskname
-> priority order
-> timestamp
-> Stauts

'''


class TodoList(models.Model):
    id   = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, null=False, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=None)
    todolistname = models.CharField(max_length=100, blank=True, null=True)

class Tasks(models.Model):
    todolistid = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, default=None)
    taskname  = models.CharField(max_length=300, blank=True, null=True)
    priority  = models.IntegerField(blank=False, null=False, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    status    = models.BooleanField(default=False)

