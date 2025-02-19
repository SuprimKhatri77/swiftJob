from django.db import models
from job.models import *
# Create your models here.
class Apply(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]


    job = models.ForeignKey(JobCreation, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resume/',null=True,blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')


    def __str__(self):
        return f'{self.applicant.username} - {self.job.job_title} - {self.get_status_display()}'