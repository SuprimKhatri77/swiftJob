from django.shortcuts import render,redirect


def index(request):
    if request.user.is_authenticated and request.user.profile.role == 'job_creator':
        return redirect('job:job-creator')
    elif request.user.is_authenticated and request.user.profile.role == 'job_seeker':
        return redirect('job:job-seeker')
    else:
        return render(request,'base.html')