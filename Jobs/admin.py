from django.contrib import admin
from .models import MyJob
# Register your models here.
#admin.site.register(MyJob)

@admin.register(MyJob)
class MyJobAdmin(admin.ModelAdmin):
    fields= ["title","company","period","descripiton","companysign"]
    list_display=["title","company","period"]
