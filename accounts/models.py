from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    JOB_SEEKER = 'job_seeker'
    JOB_CREATOR = 'job_creator'
    ROLE_CHOICES = [
        (JOB_SEEKER, 'Job Seeker'),
        (JOB_CREATOR, 'Job Creator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='images/default.webp')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=JOB_SEEKER)

    def __str__(self):
        return self.user.username
