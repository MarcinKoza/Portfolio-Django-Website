from django.db import models
from django.conf import settings

# Create your models here.
class MyEdu(models.Model):
    level = models.CharField(max_length=64)
    univeristyname = models.CharField(max_length=128)
    univeristytopic = models.CharField(max_length=128,null=True,blank=True)
    period = models.CharField(max_length=64)
    univeristysign=models.ImageField(upload_to=settings.MEDIA_ROOT,null=True,blank=True)
    def __str__(self):
        return self.univeristyname+' '+self.univeristytopic
class MyCou(models.Model):
    topic = models.CharField(max_length=128)
    time = models.CharField(max_length=64)
    def __str__(self):
        return self.topic