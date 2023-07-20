from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from base.models import User, Employee, Company

class SignupEmployeeSerializer(serializers.Serializer):
    
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(min_length=6, write_only=True, required=True)
    password_repeat = serializers.CharField(min_length=6, write_only=True, required=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password_repeat = attrs.get('password_repeat')
        
        if password == password_repeat:
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
        return user

class CreateEmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ['firstName', 'lastName', 'postalCode', 'nationalCode', 'creditCardNumber',
                  'address', 'profilePicture', 'resume', 'nationalCardPicture']
        extra_kwargs = {'user': {'required': False}}
        
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        user.has_completed_signup  = True
        user.save()
        employee = Employee.objects.create(**validated_data)
        return employee
    
class SignupCompanySerializer(serializers.Serializer):
    
    company_name = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, min_length=6, required=True)
    password_repeat = serializers.CharField(write_only=True, min_length=6, required=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password_repeat = attrs.get('password_repeat')
        
        if password == password_repeat:
            if User.objects.filter(email=email).exists():
                msg = 'There is a user with this email!'
                raise serializers.ValidationError(msg, code='conflict')
        else:
            msg = 'Informations must be entered correctly!'
            raise serializers.ValidationError(msg, code='authorization')
        
        return attrs
    
    def create(self, validated_data):
        company_name = validated_data['company_name']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        
        user = User.objects.create_user(email=email, password=password, is_company=True, has_completed_signup=True)
        Company.objects.create(user=user, name=company_name, employerFirstName=first_name, employerLastName = last_name)
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
        attrs['completed_signup'] = user.has_completed_signup
        return attrs
    
    
# CRUD Serializers

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = "__all__"
        extra_kwargs = {'user': {'required': False, 'read_only': True}}
        
class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {'user': {'required': False, 'read_only': True}}