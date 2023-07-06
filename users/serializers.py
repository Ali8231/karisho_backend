from django.contrib.auth import authenticate
from rest_framework import serializers
from base.models import user

class SingupEmployeeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, write_only=True)
    password_repeat = serializers.CharField(min_length=6, write_only=True)
    token = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password_repeat = attrs.get('password_repeat')
        
        if email and password and password_repeat and (password == password_repeat):
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            
            if user:
                msg = 'There is a user with this info!'
                raise serializers.ValidationError(msg, code='conflict')
        else:
            msg = 'Informations must be entered correctly!'
            raise serializers.ValidationError(msg, code='authorization')
        
        return attrs
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        
        user = user.objects.create_user(email, password)
        return user