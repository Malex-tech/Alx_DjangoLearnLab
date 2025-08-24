from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Read: everyone authenticated
    Write: only owner of the object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, "author_id", None) == getattr(request.user, "id", None)

class IsOwnerOrReadOnly(BasePermission):
    """
    Read for everyone; write only if you're the owner.
    Works for Post(author) and Comment(author).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return getattr(obj, "author_id", None) == getattr(request.user, "id", None)
