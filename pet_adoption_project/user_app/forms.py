from django import forms 
from.models import user_details,adoption_application

class user_form(forms.ModelForm):
    class Meta:
        model = user_details
        fields = ['username','phone_no','email','password']



class application_form(forms.ModelForm):
    class Meta:
        model = adoption_application
        fields = ['username','phone_no','email']