from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        
    
class Skill(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
class Experience(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
class JobCreation(models.Model):
    job_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_description = models.TextField()
    min_price = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    max_price = models.IntegerField(validators=[MinValueValidator(0)])
    min_time = models.IntegerField(validators=[MinValueValidator(0)])
    max_time = models.IntegerField(validators=[MinValueValidator(0)])
    location = models.CharField(max_length=50,null=True,blank=True)
    required_skills = models.ManyToManyField(Skill)
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=True,blank=True)


    def __str__(self):
        return f'{self.job_creator.username} - {self.job_title}'
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.job_title)

            existing_slug = JobCreation.objects.filter(slug=self.slug).exists()
            count = 1
            while existing_slug:
                self.slug = f"{slugify(self.job_title)}-{count}"
                existing_slug = JobCreation.objects.filter(slug=self.slug).exists()
                count += 1
        super().save(*args,**kwargs)



    

    

