# coding=utf-8

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from task.models import Task
from task.serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from task.permissions import IsOwnerOrReadOnly
import ipdb


class TaskList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'TaskList.html'
    permission_classes = (AllowAny,)
    authentication_classes = (BasicAuthentication,)

    def get(self, request):
        """
        :param request:
        :return: 返回所有任务列表
        """
        # ipdb.set_trace()
        screen = request.GET.get('screen')
        if screen == u'ALL_NOT_FINISHED':
            tasks = Task.objects.filter(finished__exact=0)
        elif screen == u"SORT_BY_CREATED_DATE":
            tasks = Task.objects.all().order_by('-created')
        elif screen == u'SORT_BY_EXPIRE_DATE':
            tasks = Task.objects.all().order_by('-expire_date')
        elif screen == u'SORT_BY_PRIORITY':
            tasks = Task.objects.all().order_by('-priority')
        else:
            tasks = Task.objects.all()
        return Response({'tasks': tasks})

    def post(self, request):
        """
        :param request:
        :return:
        """
        # ipdb.set_trace()

        owner = request.user
        serializer_context = {'request': request, }
        serializer = TaskSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(owner=owner)
            return self.get(request)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'TaskDetail.html'
    permission_classes = (AllowAny,)
    authentication_classes = (BasicAuthentication,)

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return Response({'task': task})

    def put(self, request, pk):
        # ipdb.set_trace()
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        # 如果put失败了就  返回400bad
        if not serializer.is_valid():
            ipdb.set_trace()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'task': get_object_or_404(Task, pk=pk)})

    def delete(self, request, pk):
        # ipdb.set_trace()
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        # ipdb.set_trace()
        return Response({'task': None})

    # 按理说这里不应该有post的 但是发来的HTTP request不进入另外两个函数
    def post(self, request, pk):
        # ipdb.set_trace()
        if request.data['_method'] == u'DELETE':
            # del request.data['_method']
            response = self.delete(request, pk)
            return response

        elif request.data['_method'] == u'PUT':
            # del request.data['_method']
            response = self.put(request, pk)
            return response


# 用户页面是只读的 使用ListAPIView 和 RetrieveAPIView
class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'UserList.html'

    def get(self, request):
        users = User.objects.all()
        return Response({'users': users})


class UserDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'UserDetail.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(user, context=serializer_context)
        return Response({'serializer': serializer, 'user': user})

    def post(self, request, pk):
        serializer_context = {
            'request': request,
        }
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, context=serializer_context)
        if not serializer.is_valid():
            print "Serialzer is not Valid"
            return Response({'serializer': serializer, 'user': user})
        serializer.save()
        return redirect('user-list')


class CreateUserView(CreateAPIView):
    model = User
    # permission_classes = [permissions.AllowAny] #所有人都可以注册
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'task': reverse('task-list', request=request, format=format)
    })
