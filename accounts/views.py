from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



# Create your views here.

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user = login(request,user)
            messages.success(request,'Registration successful. Welcome!')
            user_profile = request.user.profile
            if user_profile.role == 'job_seeker':
                return redirect('job:job-seeker')
            elif user_profile.role == 'job_creator':
                return redirect('job:job-creator')
        else:
            messages.error(request,'Registration failed. Please check the form')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,'Logged in successfully!')
            user_profile = request.user.profile
            if user_profile.role == 'job_seeker':
                return redirect('job:job-seeker')
            elif user_profile.role == 'job_creator':
                return redirect('job:job-creator')
        else:
            messages.error(request,'Error Logging in, Please Try again!')

    else:
        form = LoginForm()

    return render(request,'accounts/login.html',{'form':form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('/')
        