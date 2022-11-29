from django.forms import ModelForm
from .models import MyJob

class MyJobForm(ModelForm):
    class Meta:
        model=MyJob
        fields=['title', 'company', 'period', 'descripiton', 'companysign']