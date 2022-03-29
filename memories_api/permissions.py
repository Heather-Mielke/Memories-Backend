from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METTHODS:
            return True
        else:
            return obj.owner == request.user
