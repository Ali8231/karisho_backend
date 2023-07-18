from django.urls import path
from users.views import (
    SignupEmployeeApi, SignupCompanyApi, EmailLoginApi, LogoutApi,
    CreateEmployeeApi
)

urlpatterns = [
    path('signup-employee/', SignupEmployeeApi.as_view(), name='signup-employee'),
    path('signup-employee/info/', CreateEmployeeApi.as_view(), name='create-employee'),
    path('signup-company/', SignupCompanyApi.as_view(), name='signup-company'),
    path('login/', EmailLoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),
]
