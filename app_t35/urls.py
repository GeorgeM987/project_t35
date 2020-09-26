from django.urls import path
#
from .views import *

app_name = 'app_t35'

urlpatterns = [
    path('about/', about, name='about'),
    path('', home, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('price/', price, name='price'),
]