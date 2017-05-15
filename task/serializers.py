# coding=utf-8
import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    expire_date = serializers.DateField()

    def validate(self, data):
        if datetime.date.today() > data['expire_date']:
            raise serializers.ValidationError("Expire Time Must After Created Time")
        else:
            return data

    class Meta:
        model = Task
        fields = ('url', 'id', 'owner', 'created', 'title', 'content', 'finished', 'priority', 'expire_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    # owner = serializers.ReadOnlyField(source='owner.username')
    # password = serializers.CharField(write_only=True)
    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'task')
