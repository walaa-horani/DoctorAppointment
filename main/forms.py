from django import forms
from .models import Patient,Doctor

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields =('full_name','mobile_no','email','next_visit_date','address', 'detail')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'custom-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'custom-control'}),
            'address': forms.Textarea(attrs={'class': 'custom-control'}),
            'email': forms.EmailInput(attrs={'class': 'custom-control'}),
            "visit_date": forms.DateInput(attrs={'class': 'custom-control'}),
            'detail': forms.Textarea(attrs={'class': 'custom-control'}),
            'next_visit_date': forms.DateInput(attrs={'class': 'custom-control'}),
            
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields =('full_name','mobile_no','email', 'department')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'custom-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'custom-control'}),
           
            'email': forms.EmailInput(attrs={'class': 'custom-control'}),
            'department': forms.Select(attrs={'class': 'custom-select'}),
            
        }
