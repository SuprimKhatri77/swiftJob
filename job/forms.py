from django import forms
from .models import *

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = JobCreation
        fields = ['job_title','job_description','required_skills','category','experience','location','min_price','max_price','min_time','max_time',]


    required_skills = forms.ModelMultipleChoiceField(
    queryset=Skill.objects.all(),
    widget=forms.CheckboxSelectMultiple
    )






       
