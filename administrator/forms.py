from django.contrib.auth.models import User
from django.db.models import fields
from administrator.models import Budget, Department, Head
from django import forms
from django.contrib.auth.forms import UserCreationForm


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'

class HeadForm(forms.ModelForm):
    join_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    
    class Meta:
        model = Head
        fields = ['department','join_date']
        widgets = {'department':forms.Select(attrs={'class':'form-control'})}

class createUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username..'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email..'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']