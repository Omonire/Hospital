from django import forms
from .models import Referral
from patients.models import Patient
from departments.models import Department

class ReferralForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    to_department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Referral
        fields = ['patient', 'to_department']
