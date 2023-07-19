from django.urls import path
from users.views import (
    SignupEmployeeApi, SignupCompanyApi, EmailLoginApi, LogoutApi,
    CreateEmployeeApi, GetEmployeeApi, UpdateEmployeeApi, DeleteEmployeeApi,
    GetCompanyApi, UpdateCompanyApi, DeleteCompanyApi,
)

urlpatterns = [
    
    # Authentication URLs
    path('signup-employee/', SignupEmployeeApi.as_view(), name='signup-employee'),
    path('signup-employee/info/', CreateEmployeeApi.as_view(), name='create-employee'),
    path('signup-company/', SignupCompanyApi.as_view(), name='signup-company'),
    path('login/', EmailLoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),
    
    # Employee URLs
    path('employee/get/', GetEmployeeApi.as_view(), name='get-employee'),
    path('employee/update/', UpdateEmployeeApi.as_view(), name='update-employee'),
    path('employee/delete/', DeleteEmployeeApi.as_view(), name='delete-employee'),
    
    # Company URLs
    path('company/get/', GetCompanyApi.as_view(), name='get-company'),
    path('company/update/', UpdateCompanyApi.as_view(), name='update-company'),
    path('company/delete/', DeleteCompanyApi.as_view(), name='delete-company'),
    
]
