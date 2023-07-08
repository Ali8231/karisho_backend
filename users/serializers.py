from django.contrib.auth import authenticate
from rest_framework import serializers
from base.models import User, Employee

class SingupEmployeeSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(min_length=6, write_only=True)
    password_repeat = serializers.CharField(min_length=6, write_only=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password_repeat = attrs.get('password_repeat')
        
        if email and password and password_repeat and (password == password_repeat):
            if User.objects.filter(email=email).exists():
                msg = 'There is a user with this email!'
                raise serializers.ValidationError(msg, code='conflict')
        else:
            msg = 'Informations must be entered correctly!'
            raise serializers.ValidationError(msg, code='authorization')
        
        return attrs
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        
        user = User.objects.create_user(email, password, is_employee=True)
        Employee.objects.create(user=user)
        return user
    
class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            role = ""
            
            if not user:
                msg = 'Invalid email or password.'
                raise serializers.ValidationError(msg, code='authorization')
            
            if user.is_employee:
                role = "Employee"
            elif user.is_company:
                role = "Company"
            elif user.is_manager:
                role = "Manager"
            else:
                role = "Supporter"

        else:
            msg = 'Must include email and password.'
            raise serializers.ValidationError(msg, 'authorization')
        
        attrs['user'] = user
        attrs['role'] = role
        return attrs
            