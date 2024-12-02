from django import forms
from contactus.models import Contactus

class ContactusForm(forms.ModelForm):

    class Meta:
        model = Contactus
        fields = ['name', 'email', 'subject', 'message']

