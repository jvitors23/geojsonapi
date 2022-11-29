from rest_framework import permissions


class OwnProviderPermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own providers
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj here is a Provider instance
        return obj.owner == request.user
