from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serialiser import TaskSerializer
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated




@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    User.objects.create_user(username=username, password=password)
    return Response("User created successfully")
    
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    c=auth.authenticate(username=username, password=password)
    if c:
        refresh=RefreshToken.for_user(c)
        return Response({'refresh':str(refresh),'access':str(refresh.access_token)})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(request):
    task=Task.objects.filter(user=request.user)
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def task_update(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)
    return Response("Task updated successfully")
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def task_partial_update(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)
    return Response("Task updated successfully")

@api_view(['DELETE'])       
@permission_classes([IsAuthenticated])
def task_delete(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return Response("Task deleted successfully")

@api_view(['POST'])
def login (request):
    a=request.data.get('username')
    b=request.data.get('password')
    c = auth.authenticate(username=a, password=b)
    if c:
        refresh=RefreshToken.for_user(c)
        return Response({"refresh":str(refresh), "access":str(refresh.access_token)})


@api_view(['POST'])
def register (request):
    a = request.data.get('username')
    b = request.data.get('password')
    User.objects.create_user(username=a, password=b)
    return Response("User created successfully")

# Create your views here.
