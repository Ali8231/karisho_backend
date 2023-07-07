# Register, Login and Logout URLs

from django.urls import path
from users.views import SingupEmployeeApiView

urlpatterns = [
    path('signup-employee/', SingupEmployeeApiView.as_view(), name='signup-employee')
]
