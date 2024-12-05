from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vakanсy, ChildProfile, CustomUser
from django.contrib.auth.models import AbstractUser

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class PostForm(forms.ModelForm):
    class Meta:
        model = Vakanсy
        fields = ['name', 'category', 'author', 'cost', 'phone', 'course']



class ParentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'parent'
        if commit:
            user.save()
        return user

# Регистрация ребёнка
class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = ChildProfile
        fields = ['school_name', 'grade']


class EmployerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employer'
        if commit:
            user.save()
        return user


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vakanсy
        fields = ['name', 'cost', 'author', 'phone']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['employer'].queryset = CustomUser.objects.filter(role='employer')