# coding=utf-8
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定权限 只有创建者可以编辑
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
