from django.urls import path
#
from .views import *

app_name = 'app_users'

urlpatterns = [
    path('users/', users, name='users'),
    path('users/register', register, name='register'),
    path('users/login', log_in, name='login'),
    path('users/logout', log_out, name='logout'),
    path('users/customer', customer, name='customer'),
]