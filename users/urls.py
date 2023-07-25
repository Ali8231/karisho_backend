from django.urls import path
from users.views import (
    SignupEmployeeApi, SignupCompanyApi, EmailLoginApi, LogoutApi,
    CreateEmployeeApi, GetUpdateEmployeeApi, DeleteEmployeeApi,
    GetUpdateCompanyApi, DeleteCompanyApi,
)

urlpatterns = [
    
    # Authentication URLs
    path('signup-employee/', SignupEmployeeApi.as_view(), name='signup-employee'),
    path('signup-employee/info/', CreateEmployeeApi.as_view(), name='create-employee'),
    path('signup-company/', SignupCompanyApi.as_view(), name='signup-company'),
    path('login/', EmailLoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),
    
    # Employee URLs
    path('employee/', GetUpdateEmployeeApi.as_view(), name='get-update-employee'),
    path('employee/delete/', DeleteEmployeeApi.as_view(), name='delete-employee'),
    
    # Company URLs
    path('company/', GetUpdateCompanyApi.as_view(), name='get-update-company'),
    path('company/delete/', DeleteCompanyApi.as_view(), name='delete-company'),
    
]
