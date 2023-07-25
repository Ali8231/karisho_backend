from rest_framework.permissions import BasePermission

class HasCompletedSignup(BasePermission):
    
    message = "You must complete your signup to access this resource."
    
    def has_permission(self, request, view):
        return request.user.has_completed_signup