from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import MyEdu,MyCou
from django.contrib.auth.decorators import login_required
from Skills.models import MySkill


# Create your views here.
def Edu_response(request):
    all_edu = MyEdu.objects.all().order_by('-period')
    all_cou = MyCou.objects.all()
    all_skills = MySkill.objects.all().order_by('-level')
    return render(request,"Edcuation.html",{"education":all_edu,"courses":all_cou,"skills":all_skills})