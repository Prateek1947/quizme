from rest_framework.permissions import BasePermission


class IsAuthenticatedOrPostOnly(BasePermission):
    """
    Allows to create new user and read without authentication
    """

    def has_permission(self, request, view):
        if request.method == "POST" or request.method == "GET":
            return True
        return request.user and request.user.is_authenticated
