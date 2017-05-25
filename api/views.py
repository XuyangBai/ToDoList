# coding=utf-8
from rest_framework import viewsets, authentication, permissions, filters
from task.models import Task
from task.permissions import IsOwnerOrReadOnly
from task.serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters import FilterSet


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = ('title', 'content')


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ('username', 'email')


class DefaultsMixin(object):
    authentication_classes = (authentication.BasicAuthentication, authentication.TokenAuthentication)
    permissions_classes = (permissions.IsAuthenticated)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    search_fields = ('username','email')


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    search_fields = ('title', 'content')
