from django.contrib import admin
from todolistcore.models import TodoList, Tasks
# Register your models here.

admin.site.register(TodoList)
admin.site.register(Tasks)
