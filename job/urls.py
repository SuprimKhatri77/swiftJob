from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
     path('job-seeker/',views.job_seeker_view,name='job-seeker'),
     path('job-creator/',views.job_creator_view,name='job-creator'),
     path('job-creation-form/',views.job_creation_view,name='job-creation-form'),
     path('avialable-jobs/',views.available_jobs_view,name='avialable-jobs'),
]
