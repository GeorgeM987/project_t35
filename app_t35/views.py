from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#
from app_users.decorators import unauthenticated_user, allowed_users
from .maps import *

def about(request):
    context = {'title': 'About'}
    return render(request, 'app_t35/about.html', context)

def home(request):
    context = {'title': 'HomePage'}
    return render(request, 'app_t35/home.html', context)

@login_required(login_url='app_users:login')
@allowed_users(allowed_roles=['admin', 'staff', 'users'])
def price(request):
    # url = search()
    # this_map = best_route(url)
    context = {'title': 'Pricing', 'this_map': 'this_map'}
    return render(request, 'app_t35/price.html', context)

@login_required(login_url='app_users:login')
@allowed_users(allowed_roles=['admin', 'staff'])
def dashboard(request):
    context = {'title': 'Dashboard'}
    return render(request, 'app_t35/dashboard.html', context)
