from django import forms 
from.models import pet_details

class pet_forms(forms.ModelForm):
    class Meta:
        model = pet_details
        fields = ['pet_name','pet_breed','pet_age','pet_image']

