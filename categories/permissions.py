from rest_framework.permissions import BasePermission

class IsAdminOrStaffUser(BasePermission):
    
    # Allows access only to admin and staff users.

    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.is_superuser)
