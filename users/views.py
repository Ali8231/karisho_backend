from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from base.models import User, Employee, Company
from users.permissions import HasCompletedSignup
from users.serializers import (
    SignupEmployeeSerializer, CreateEmployeeSerializer, SignupCompanySerializer, EmailLoginSerializer,
    EmployeeSerializer, CompanySerializer
)

# Authentication APIs
class SignupApi(generics.CreateAPIView): # parent of sign-up API views
    
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        new_user = User.objects.get(email=serializer.validated_data['email'])
        token, created = Token.objects.get_or_create(user=new_user)
        data = {
            'token': token.key,
            'user_id': new_user.id,
            'is_company': new_user.is_company,
            'is_employee': new_user.is_employee,
            'completed_signup': new_user.has_completed_signup,
        }
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class SignupEmployeeApi(SignupApi):
    
    serializer_class = SignupEmployeeSerializer
    
class SignupCompanyApi(SignupApi):
    
    serializer_class = SignupCompanySerializer
    
class EmailLoginApi(generics.GenericAPIView):
    
    permissions = [permissions.AllowAny]
    serializer_class = EmailLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        role = serializer.validated_data['role']
        completed_signup = serializer.validated_data['completed_signup']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'role': role,
            'completed_signup': completed_signup,
            'user_id': user.id,
            'is_company': user.is_company,
            'is_employee': user.is_employee
        })
        
class LogoutApi(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        Token.objects.filter(user=request.user).delete()
        return Response({"detail": "Successfully logged out."})
        
# CRUD APIs
class CreateEmployeeApi(generics.CreateAPIView):
    
    permissions = [permissions.IsAuthenticated]
    serializer_class = CreateEmployeeSerializer
    
class GetUpdateEmployeeApi(generics.RetrieveUpdateAPIView):
    
    permissions = [permissions.IsAuthenticated, HasCompletedSignup]
    serializer_class = EmployeeSerializer
    
    def get_object(self):
        return Employee.objects.get(user=self.request.user)
    
class DeleteEmployeeApi(generics.DestroyAPIView):
    
    permissions = [permissions.IsAuthenticated, HasCompletedSignup]
    
    def get_object(self):
        return self.request.user
    

class GetUpdateCompanyApi(generics.RetrieveUpdateAPIView):
    
    permissions = [permissions.IsAuthenticated, HasCompletedSignup]
    serializer_class = CompanySerializer
    
    def get_object(self):
        return Company.objects.get(user=self.request.user)
    
class DeleteCompanyApi(generics.DestroyAPIView):
    
    permissions = [permissions.IsAuthenticated, HasCompletedSignup]
    
    def get_object(self):
        return self.request.user