from django.urls import path
from . import views

app_name = 'application'  



urlpatterns = [
    path('job-application-form/<slug:slug>/',views.job_application_view,name='job-application-form'),
    path('applications/',views.application_view,name='applications') ,
    path('application-detail/<int:id>/',views.view_application_details,name='application-detail'),
    path('application/accpet/<int:id>/',views.accept_application,name='accept-application'),
    path('application/reject/<int:id>/',views.reject_application,name='reject-application'),
    path('recent-applications-all/',views.recent_applications,name='recent-applications-all')
]
