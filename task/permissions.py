# coding=utf-8
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定权限 只有创建者可以编辑
    """
    def has_object_permission(self, request, view, obj):
        # 这种方式是只要是get都可以返回 也就是说 所有人都可以看到别人的任务
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # else:
        #     return obj.owner == request.user
        return obj.owner == request.user