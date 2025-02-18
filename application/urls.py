from django.urls import path
from . import views

app_name = 'application'  



urlpatterns = [
    path('job-application-form/<slug:slug>/',views.job_application_view,name='job-application-form'),
    path('applications/',views.application_view,name='applications') ,
    path('application-detail/<int:id>/',views.view_application_details,name='application-detail')
]
