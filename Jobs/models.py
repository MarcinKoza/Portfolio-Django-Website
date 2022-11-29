from django.db import models
from django.conf import settings

# Create your models here.
class MyJob(models.Model):
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    period = models.CharField(max_length=64)
    descripiton= models.TextField(default="")
    companysign=models.ImageField(upload_to=settings.MEDIA_ROOT,null=True,blank=True)

    def __str__(self):
        return self.title+' '+self.company
