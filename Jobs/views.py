from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import MyJob,JobDuty
from Skills.models import MySkill
from .forms import MyJobForm
from django.contrib.auth.decorators import login_required


def jobs_response(request):
    all_jobs=MyJob.objects.all()
    job_list=[]
    for job in all_jobs:
        job_duties=job.jobduty_set.all()
        job_list.append({"job":job,"duties":job_duties})
    all_skills = MySkill.objects.all().order_by('-level')
    return render(request,"Jobs.html",{"jobs":job_list,"skills":all_skills,})


@login_required
def new_job_response(request):
    form = MyJobForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(jobs_response)

    return render(request,"NewJob.html", {'form':form})

@login_required
def edit_job_response(request,id):
    job=get_object_or_404(MyJob,pk=id)
    form = MyJobForm(request.POST or None, request.FILES or None,instance=job)

    if form.is_valid():
        form.save()
        return redirect(jobs_response)

    return render(request,"EditJob.html", {'form':form})

@login_required
def delete_job_response(request,id):
    job=get_object_or_404(MyJob,pk=id)

    if request.method == "POST":
        job.delete()
        return redirect(jobs_response)

    return render(request,"Accept.html", {'item':job})