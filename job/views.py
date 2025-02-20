from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from application.models import *
from django.db.models import Q
# Create your views here.
def job_creator_view(request):
    jobs = JobCreation.objects.filter(job_creator=request.user).order_by('-created_at')
    recent_applications = Apply.objects.filter(job__in=jobs).order_by('-date_applied')[:3]
    acitve_jobs_count = JobCreation.objects.filter(job_creator=request.user).count()
    total_applications = Apply.objects.filter(job__in=jobs).count()
    pending_count = Apply.objects.filter(job__in=jobs, status='in_progress').count()
    hired_count = Apply.objects.filter(job__in=jobs, status='accepted').count()
    shortlisted_count = Apply.objects.filter(job__in=jobs, status="accepted").count()
    print(jobs)
    context = {
        'jobs':jobs,
        'recent_applications':recent_applications,
        'active_jobs_count':acitve_jobs_count,
        'total_applications':total_applications,
        'pending_count':pending_count,
        'hired_count':hired_count,
    }
    return render(request,'job/job_creator.html',context)


def job_seeker_view(request):
    jobs = JobCreation.objects.all().order_by('-created_at')
    applications = Apply.objects.filter(applicant=request.user).order_by('-date_applied')[:3]
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
    query = request.GET.get('q', '')
    jobs = JobCreation.objects.all().order_by('-created_at')
    search_results = []
    if query:
        search_results = jobs.filter(Q(job_title__icontains=query) | Q(category__name__icontains=query) | Q(required_skills__name__icontains=query)).distinct()
    else:
        search_results = jobs
    context = {
        'jobs':jobs,
        'query':query,
        'search_results':search_results
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



@login_required
def edit_job_application_form(request,id):
    job = get_object_or_404(JobCreation, id=id, job_creator=request.user)
    if request.method == 'POST':
        form = EditJobCreationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job:job-creator')
    else:
        form = EditJobCreationForm(instance=job)
    return render(request,'job/edit_job_form.html',{'form':form})



@login_required
def delete_job_application_form(request,id):
    job = get_object_or_404(JobCreation, id=id, job_creator=request.user)
    if request.method == 'POST':
        form = DeleteJobCreationForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            job.delete()
            return redirect('job:job-creator')
    else:
        form = DeleteJobCreationForm()
    return render(request,'job/delete_job_form.html',{'form':form,'job':job})




            



    
