from django.contrib import admin
from .models import MyEdu,MyCou


# Register your models here.
# admin.site.register(MyJob)
@admin.register(MyEdu)
class MyEduAdmin(admin.ModelAdmin):
    fields = ["level", "univeristyname", "period","univeristysign", "univeristytopic"]
    list_display = ["level", "univeristyname","period"]

@admin.register(MyCou)
class MyCouAdmin(admin.ModelAdmin):
    fields = ["topic", "time",]
    list_display = ["topic", "time"]

