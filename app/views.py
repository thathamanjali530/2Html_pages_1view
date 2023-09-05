from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


# Create your views here.

def htmlforms(request):
    if request.method=='POST':
        scn=request.POST['scn']
        scp=request.POST['sp']
        slo=request.POST['sl']
        SO=school.objects.get_or_create(scname=scn,scprincipal=scp,sclocation=slo)[0]
        SO.save()

        QLSO=school.objects.all()
        d={'QLSO':QLSO}


        return render(request,'display_school.html',d)

    return render(request,'htmlforms.html')

def insert_student(request):
    if request.method=='POST':
        scn=request.POST['scn']
        stn=request.POST['stn']
        id=request.POST['id']

        SO=school.objects.get(scname=scn)

        STO=student.objects.get_or_create(scname=SO,sname=stn,sid=id)[0]
        STO.save()

        QLSTO=student.objects.all()
        d={'QLSTO':QLSTO}
        return render(request,'display_student.html',d)
    return render(request,'insert_student.html')


