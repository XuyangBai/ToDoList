# coding=utf-8
from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User


#  owner放在那个里面无所谓吗？

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = ('url','id','owner','created','title','content','expire_date')


class UserSerializer(serializers.ModelSerializer):

    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('url','username','task')