from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ToDo.models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ToDo.Serializers import MySerializer


def MyHome(request):
    return HttpResponse("Hello I am Django App")
@api_view(["GET"])
def Task_List(request):
    task_list=Task.objects.all()
    all_data=MySerializer(task_list,many=True)
    return Response(all_data.data)
def DeleteTask(request,TaskId):
    Onetask=Task.objects.get(id=TaskId)
    Onetask.delete()
    return Response("you Deleted Task")

@api_view(["POST"])
def CreateData(request):
    print(request.data)
    serializer = MySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("You created new Task..")

@api_view(["POST"])
def UpdateData(request,TaskId):
    Onetask = Task.objects.get(id=TaskId)
    serializer = MySerializer(instance=Onetask,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("You have udated your Task..")

