from django.db import models
from job.models import *
# Create your models here.
class Apply(models.Model):
    job = models.ForeignKey(JobCreation, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resume/',null=True,blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.applicant.username} - {self.job.job_title}'