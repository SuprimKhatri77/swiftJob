from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile_picture = self.cleaned_data.get('profile_picture')
            role = self.cleaned_data.get('role')
            profile = Profile.objects.create(user=user, profile_picture=profile_picture, role=role)
            profile.save()
        return user
    


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
