from rest_framework import permissions
from base.models import User, Company, Job

class IsCompany(permissions.BasePermission):

    def has_permission(self, request, view):
        user = User.objects.get(id=request.user.id)
        if user.is_company == True :
            return True
        else:
            return False
        

class DoesOwnAdd(permissions.BasePermission):

    def has_permission(self, request, view):
        job = Job.objects.get(id=view.kwargs['job_id'])
        company = Company.objects.get(user=request.user)
        if company.user_id == job.company.user_id :
            return True
        else:
            return False