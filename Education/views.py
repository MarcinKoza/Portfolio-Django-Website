from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import MyEdu,MyCou
from django.contrib.auth.decorators import login_required
from Skills.models import MySkill
from .forms import MyEduForm,MyCouForm


# Create your views here.
def Edu_response(request):
    all_edu = MyEdu.objects.all().order_by('-period')
    all_cou = MyCou.objects.all()
    all_skills = MySkill.objects.all().order_by('-level')
    return render(request,"Edcuation.html",{"education":all_edu,"courses":all_cou,"skills":all_skills})


@login_required
def new_edu_response(request):
    form = MyEduForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(Edu_response)

    return render(request,"NewSchool.html", {'form':form})

@login_required
def edit_edu_response(request,id):
    Edu=get_object_or_404(MyEdu,pk=id)
    form = MyEduForm(request.POST or None, request.FILES or None,instance=Edu)

    if form.is_valid():
        form.save()
        return redirect(Edu_response)

    return render(request,"EditSchool.html", {'form':form})

@login_required
def delete_edu_response(request,id):
    Edu=get_object_or_404(MyEdu,pk=id)

    if request.method == "POST":
        Edu.delete()
        return redirect(Edu_response)

    return render(request,"Accept.html", {'item':Edu})


@login_required
def new_cou_response(request):
    form = MyCouForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(Edu_response)

    return render(request,"NewSchool.html", {'form':form})

@login_required
def edit_cou_response(request,id):
    Cou=get_object_or_404(MyCou,pk=id)
    form = MyCouForm(request.POST or None, request.FILES or None,instance=Cou)

    if form.is_valid():
        form.save()
        return redirect(Edu_response)

    return render(request,"EditSchool.html", {'form':form})

@login_required
def delete_cou_response(request,id):
    Cou=get_object_or_404(MyCou,pk=id)

    if request.method == "POST":
        Cou.delete()
        return redirect(Edu_response)

    return render(request,"Accept.html", {'item':Cou})