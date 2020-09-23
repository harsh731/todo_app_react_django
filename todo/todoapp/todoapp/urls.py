
from django.contrib import admin
from django.urls import path
from ToDo.views import MyHome, Task_List,DeleteTask,CreateData,UpdateData




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', MyHome),
    path('task_list/', Task_List),
    path('delete_task/<int:TaskId>/',DeleteTask),
    path('update_task/<int:TaskId>/',UpdateData),
    path('create_task/',CreateData),
]
