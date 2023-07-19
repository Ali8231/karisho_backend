from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from base.models import *

class postAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ['jobTitle', 'jobDescription', 'picture', 'requiredSkills', 
                  'rules' , 'category', 'subCategory', 'address']
        extra_kwargs = {'company': {'required': False, 'read_only': True},
                        'minimumHourlySalary': {'required': False, 'read_only': True}}
        
    def create(self, validated_data):
        company = Company.objects.get(user=self.context['request'].user)
        validated_data['company'] = company
        job = Job.objects.create(**validated_data)
        return job
    

class createShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = ['date', 'startTime', 'endTime', 'salary']
        extra_kwargs = {'job': {'required': False, 'read_only': True},
                        'numberOfApplicants': {'required': False, 'read_only': True}}
