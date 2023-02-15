from django.forms import ModelForm
from .models import MySkill

class MySkillForm(ModelForm):
    class Meta:
        model=MySkill
        fields=['name', 'level', 'techlogo', ]