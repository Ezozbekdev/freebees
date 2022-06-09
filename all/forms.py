from django.forms import forms
from .models import Contect
from django.forms.models import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contect
        fields = '__all__'
