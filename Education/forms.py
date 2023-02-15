from django.forms import ModelForm
from .models import MyEdu, MyCou

class MyEduForm(ModelForm):
    class Meta:
        model=MyEdu
        fields=['level', 'univeristyname', 'univeristytopic', 'period', 'univeristysign', ]

class MyCouForm(ModelForm):
    class Meta:
        model=MyCou
        fields=['topic', 'time',]