# coding=utf-8
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from task.models import Task
from task.serializers import TaskSerializer,UserSerializer
from django.contrib.auth.models import User
from  rest_framework import permissions
from task.permissions import IsOwnerOrReadOnly

class TaskList(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    #现在create方法将会获得一个新的字段 owner 是request中的user信息
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, )


# 用户页面是只读的 使用ListAPIView 和 RetrieveAPIView
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'task': reverse('task-list', request=request, format=format)
    })


def test(request):
    return render(request, 'index.html')


