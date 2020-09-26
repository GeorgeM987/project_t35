from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
#
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from .decorators import unauthenticated_user, allowed_users
from .models import Profile


@unauthenticated_user
def users(request):
    context = {'title': 'User'}
    return render(request, 'app_users/users.html', context)

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='users')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            Profile.objects.create(users=user, phone=phone)
            messages.success(request, 'Account created for {}'.format(username))
            login(request, user)
            return redirect('app_users:customer')
    else:
        form = UserRegisterForm()
    context = {'title': 'Register', 'form': form}
    return render(request, 'app_users/register.html', context)

@unauthenticated_user
def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'You are now logged in as {}'.format(username))
                return redirect('app_users:customer')
        else:
            messages.error(request, 'Username or Password is incorrect!')
    form = UserLoginForm()
    context = {'title': 'Login', 'form': form}
    return render(request, 'app_users/login.html', context)

def log_out(request):
    logout(request)
    messages.info(request, 'You\'ve been succesfully logged out!')
    return redirect('app_t35:homepage')

@login_required(login_url='app_users:login')
@allowed_users(allowed_roles=['users', 'staff', 'admin'])
def customer(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() or profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, 'Account has been updated!')
            return redirect('app_users:customer')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'title': 'Customer', 'user_update_form': user_update_form, 'profile_update_form':profile_update_form}
    return render(request, 'app_users/customer.html', context)