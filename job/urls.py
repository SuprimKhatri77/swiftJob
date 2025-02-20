from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
     path('seeker-dashbaord/',views.job_seeker_view,name='job-seeker'),
     path('creator-dashboard/',views.job_creator_view,name='job-creator'),
     path('job-creation-form/',views.job_creation_view,name='job-creation-form'),
     path('avialable-jobs/',views.available_jobs_view,name='avialable-jobs'),
     path('job/edit-job-form/<int:id>/', views.edit_job_application_form, name='edit-job-form'),
     path('job/delete-job-form/<int:id>/', views.delete_job_application_form, name='delete-job-form'),
]
