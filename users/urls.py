# Register, Login and Logout URLs

from django.urls import path
from users.views import SignupEmployeeApiView, SignupCompanyApiView, EmailLoginApiView

urlpatterns = [
    path('signup-employee/', SignupEmployeeApiView.as_view(), name='signup-employee'),
    path('signup-company/', SignupCompanyApiView.as_view(), name='signup-company'),
    path('login/', EmailLoginApiView.as_view(), name='login')
]
