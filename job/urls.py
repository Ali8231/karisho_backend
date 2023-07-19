from django.urls import path
from job.views import *
urlpatterns = [
    path('post-add/', postAdd.as_view(), name='post-add'),
    path('post-add/<job_id>/create-shift', createShift.as_view(), name='create-shift'),
]