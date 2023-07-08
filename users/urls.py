# Register, Login and Logout URLs

from django.urls import path
from users.views import SingupEmployeeApiView, EmailLoginApiView

urlpatterns = [
    path('signup-employee/', SingupEmployeeApiView.as_view(), name='signup-employee'),
    path('login/', EmailLoginApiView.as_view(), name='login')
]
