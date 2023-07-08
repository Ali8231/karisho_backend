from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from base.models import User
from users.serializers import SingupEmployeeSerializer, EmailLoginSerializer

class SingupEmployeeApiView(generics.CreateAPIView):
    
    serializer_class = SingupEmployeeSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        new_user = User.objects.get(email=serializer.validated_data['email'])
        token, created = Token.objects.get_or_create(user=new_user)
        data = {
            'token': token.key
        }
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
class EmailLoginApiView(generics.GenericAPIView):
    permissions = [permissions.AllowAny]
    serializer_class = EmailLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        role = serializer.validated_data['role']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'role': role
        })