from django.db import models
from django.conf import settings

# Create your models here.
class MySkill(models.Model):
    name = models.CharField(max_length=64)
    skill_levels = (
        ('1', 'Beginner'),
        ('2', 'Advanced'),
        ('3', 'Competent'),
        ('4', 'Proficient'),
        ('5', 'Expert'),
    )
    level = models.CharField(max_length=1, choices=skill_levels)
    techlogo = models.ImageField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)

    def __str__(self):
        return self.name+' '+self.level
