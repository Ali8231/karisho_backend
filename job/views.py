from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from job.permissions import *
from base.models import *
from job.serializers import *

class postAdd(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCompany]
    serializer_class = AddSerializer

class createShift(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCompany, DoesOwnAdd]
    serializer_class = ShiftSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_id = kwargs['job_id']
        job = Job.objects.get(id=job_id)
        job.has_shift = True
        job.save()
        serializer.validated_data['job'] = job
        shift = Shift.objects.create(**serializer.validated_data)
        data = {
            'date': shift.date,
            'startTime': shift.startTime,
            'endTime': shift.endTime,
            'salary': shift.salary,
            'job_id': shift.job.id,
        }
        return Response(data=data ,status=status.HTTP_201_CREATED)

