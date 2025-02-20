from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from job.models import *
from django.db.models import Case, When, Value, IntegerField
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
    applications = Apply.objects.filter(job__in=jobs).annotate(
        status_order=Case(
            When(status='in_progress', then=Value(1)),
            When(status='accepted', then=Value(2)),
            When(status='rejected', then=Value(3)),
            output_field=IntegerField(),
        )
    ).order_by('status_order')
    context = {
        'applications':applications
    }
    return render(request,'application/application.html',context)




@login_required
def view_application_details(request,id):
    application = get_object_or_404(Apply, id=id)
    applications = Apply.objects.filter(id=id)
    if application.job.job_creator != request.user:
        return redirect('/')
    context = {
        'application': application,
        'applications':applications
    }
    return render(request,'application/view_application_detail.html',context)



@login_required
def accept_application(request,id):
    if request.method == 'POST':
        application = get_object_or_404(Apply, id=id)
        application.status = 'accepted'
        application.save()
        return redirect('application:applications')
    
@login_required
def reject_application(request,id):
    if request.method == 'POST':
        application = get_object_or_404(Apply, id=id)
        application.status  = 'rejected'
        application.save()
        return redirect('application:applications')
    

@login_required
def recent_applications(request):
    status = request.GET.get('status', '')
    order = request.GET.get('order', '')
    applications = Apply.objects.filter(applicant=request.user).order_by('-date_applied')

    if status and status != 'all':
        applications =  applications.filter(status=status)
    if order == 'newest':
        applications = applications.all().order_by('-date_applied')
    elif order == 'oldest':
        applications = applications.all().order_by('date_applied')
    else:
        order = 'newest'
    context = {
        'applications':applications,
        'status':status,
        'order':order
    }
    return render(request,'application/recent_applications.html',context)
    
        
