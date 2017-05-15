# coding=utf-8
import ipdb
from rest_framework import permissions


class IsOwnerOrNoPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ipdb.set_trace()
        return obj.owner == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # ipdb.set_trace()
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user
