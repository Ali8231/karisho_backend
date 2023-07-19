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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_id = kwargs['job_id']
        job = Job.objects.get(id=job_id)
        job.has_shift = True
        serializer.validated_data['job'] = job
        shift = Shift.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

