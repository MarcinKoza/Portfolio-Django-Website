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

class JobDuty(models.Model):
    duty = models.CharField(max_length=150)
    job = models.ForeignKey(MyJob, on_delete=models.CASCADE)
    Importances = (
        (0, 'Very Low'),
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
        (4, 'Very High'),
    )

    importance = models.IntegerField(default=0, choices=Importances)
    def __str__(self):
        return self.duty

    @property
    def  title(self):
        return self.job.title
    @property
    def  company(self):
        return self.job.company
    @property
    def  period(self):
        return self.job.period
    @property
    def  descripiton(self):
        return self.job.descripiton
    @property
    def  companysign(self):
        return self.job.companysign
    @property
    def  id(self):
        return self.job.id