from django.shortcuts import render
from .models import Person,Skill,Experience,Tag
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q
import datetime
import os

# Create your views here.
def resume_list(request):
    resume_list = Person.objects.all()
    return render(request,'resume_prac/resume_list.html',{'resume_list':resume_list})

def resume_write(request):
    # UPLOAD_DIR = '%Y/%m/%d/orig'

    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']

        oneline = request.POST['oneline']
        intro = request.POST['introduction']
        # tags = request.POST.getlist('tags')
        if 'profile_image' in request.FILES :
            profile = request.FILES['profile_image']
            person = Person.objects.create(person_name=name,position=position,profile_image=profile,person_desc=intro,person_oneline=oneline)
            person.save()
        else :
            person = Person.objects.create(person_name=name,position=position,person_desc=intro,person_oneline=oneline)
            person.save()
        #
        # for t in tags:
        #     person.tag_set.add(t)

        #경력
        ex_startdate = dict(request.POST)['startDate']
        ex_enddate = dict(request.POST)['endDate']
        ex_title = dict(request.POST)['title']
        ex_desc = dict(request.POST)['desc']
        num = 0

        for e in ex_title :
            experience = Experience.objects.create(startDate=ex_startdate[num],endDate= ex_enddate[num],ex_name=e,ex_desc=ex_desc[num],person=person)
            experience.save()
            num+= 1

        #기술 스택
        sk = dict(request.POST)['skill']
        degree = dict(request.POST)['skill_degree']
        number = 0
        for s in sk  :
            skill = Skill.objects.create(devstack=s,person= person,degree=degree[number])
            skill.save()
            number+= 1

        return HttpResponseRedirect(reverse('resume:detail', args=(person.id,)))
    else :
         return render(request,'resume_prac/resume_write.html')

def detail_add(request,resume_id):

    if request.method == 'POST':
        person = Person.objects.get(id=resume_id)
        tag_name = dict(request.POST)['tag_name']

        for t in tag_name:
            tag = Tag.objects.create(tag_name=t)
            person.tag_set.add(tag)

        return HttpResponseRedirect(reverse('resume:detail', args=(person.id,)))
    else :
         tag = Tag.objects.all
         return render(request,'resume_prac/detail_add.html',{'tag':tag})

def resume_detail(request,resume_id):
    person = Person.objects.get(id=resume_id)
    experience = person.experience_set.order_by('-startDate')
    return render(request,'resume_prac/resume_detail.html',{'person':person,'experience':experience})

def resume_templates(request,example_id):
    person = Person.objects.first()
    experience = person.experience_set.order_by('-startDate')
    if example_id == "1":
        # == 1 로 했을땐 안됐는데 "1"로 하니까 됐음
        return render(request,'resume_prac/resume_detail.html',{'person':person,'experience':experience})
    else :
        return render(request,'resume_prac/resume_detail_3.html',{'person':person,'experience':experience})

def resume_search(request):
    if request.method =="GET":
        query = request.GET.get('q')
        person = Person.objects.filter(Q(person_name__icontains=query) | Q(position__icontains=query))
        return render(request,'resume_prac/resume_list.html',{'resume_list':person})
