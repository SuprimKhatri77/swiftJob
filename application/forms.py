from django import forms
from .models import *

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['cover_letter','resume']