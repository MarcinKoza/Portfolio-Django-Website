from django.contrib import admin
from .models import MySkill
# Register your models here.
#admin.site.register(MyJob)

@admin.register(MySkill)
class MySkillAdmin(admin.ModelAdmin):
    fields= ["name","level","techlogo"]
    list_display=["name","level"]