from django.shortcuts import render,redirect
from accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from application.models import *
# Create your views here.
def job_creator_view(request):
    jobs = JobCreation.objects.filter(job_creator=request.user)
    applications = Apply.objects.filter(job__in=jobs).order_by('-date_applied')[:5]
    acitve_jobs_count = JobCreation.objects.filter(job_creator=request.user).count()
    total_applications = Apply.objects.filter(job__in=jobs).count()
    pending_count = Apply.objects.filter(job__in=jobs, status='in_progress').count()
    hired_count = Apply.objects.filter(job__in=jobs, status='accepted').count()
    shortlisted_count = Apply.objects.filter(job__in=jobs, status="accepted").count()
    print(jobs)
    context = {
        'jobs':jobs,
        'recent_applications':applications,
        'active_jobs_count':acitve_jobs_count,
        'total_applications':total_applications,
        'pending_count':pending_count,
        'hired_count':hired_count,
    }
    return render(request,'job/job_creator.html',context)


def job_seeker_view(request):
    jobs = JobCreation.objects.all().order_by('-created_at')
    applications = Apply.objects.filter(applicant=request.user)[:3]
    experiences = Experience.objects.all()
    applications_count = Apply.objects.filter(applicant=request.user).count()
    in_progress_count = Apply.objects.filter(applicant=request.user, status='in_progress').count()
    accepted_count = Apply.objects.filter(applicant=request.user, status='accepted').count()
    rejected_count = Apply.objects.filter(applicant=request.user, status='rejected').count()
    context = {
        'jobs':jobs,
        'recent_applications':applications,
        'experiences':experiences,
        'applications_count':applications_count,
        'in_progress_count':in_progress_count,
        'accepted_count':accepted_count,
        'rejected_count':rejected_count
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




            



    
