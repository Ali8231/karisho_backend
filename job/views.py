from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from job.permissions import *
from base.models import *
from job.serializers import *

class postAdd(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCompany]
    serializer_class = postAddSerializer

class createShift(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCompany, DoesOwnAdd]
    serializer_class = createShiftSerializer

