from django.shortcuts import render,redirect
from accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def job_creator_view(request):
    jobs = JobCreation.objects.filter(job_creator=request.user)
    print(jobs)
    context = {
        'jobs':jobs
    }
    return render(request,'job/job_creator.html',context)


def job_seeker_view(request):
    jobs = JobCreation.objects.all().order_by('-created_at')
    context = {
        'jobs':jobs
    }
    return render(request,'job/job_seeker.html',context)

def available_jobs_view(request):
    jobs = JobCreation.objects.all().order_by('-created_at')
    context = {
        'jobs':jobs
    }
    return render(request,'job/avialable_jobs.html',context)


@login_required
def job_creation_view(request):
    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.job_creator = request.user
            job.save()
            form.save_m2m() 
            return redirect('job:job-creator')
    else:
        form = JobCreationForm()
    return render(request,'job/job_creation_form.html',{'form':form})




            



    
