from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from job.models import *
# Create your views here.
@login_required
def job_application_view(request,slug):
    job = get_object_or_404(JobCreation, slug=slug)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request,'Application submitted successfully!')
            return redirect('job:job-seeker')
    else:
        form = JobApplicationForm()
    return render(request,'application/job_application.html',{'form':form})




@login_required
def application_view(request):
    jobs = JobCreation.objects.filter(job_creator=request.user)
    applications = Apply.objects.filter(job__in=jobs).order_by('-date_applied')
    context = {
        'applications':applications
    }
    return render(request,'application/application.html',context)




@login_required
def view_application_details(request,id):
    application = get_object_or_404(Apply, id=id)
    if application.job.job_creator != request.user:
        return redirect('/')
    context = {
        'application': application
    }
    return render(request,'application/view_application_detail.html',context)
