from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import MySkill
from Jobs.views import jobs_response
from .forms import MySkillForm
from django.contrib.auth.decorators import login_required

@login_required
def new_skill_response(request):
    form = MySkillForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(jobs_response)

    return render(request,"NewSkill.html", {'form':form})

@login_required
def edit_skill_response(request,id):
    skill=get_object_or_404(MySkill,pk=id)
    form = MySkillForm(request.POST or None, request.FILES or None,instance=skill)

    if form.is_valid():
        form.save()
        return redirect(jobs_response)

    return render(request,"EditSkill.html", {'form':form})

@login_required
def delete_skill_response(request,id):
    skill=get_object_or_404(MySkill,pk=id)

    if request.method == "POST":
        skill.delete()
        return redirect(jobs_response)

    return render(request,"Accept.html", {'item':skill})