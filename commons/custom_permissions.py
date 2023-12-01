from rest_framework.permissions import IsAuthenticated
from authentication.models import Role

class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.registereduser.role == Role.ADMIN