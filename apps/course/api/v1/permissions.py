from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.id == request.user.id

class IsOwnerForLessonOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(request)
        print(view)
        print(obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.course.author.id == request.user.id
