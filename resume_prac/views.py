from django.shortcuts import render
from .models import Person
from .models import Skill
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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
        profile = request.FILES['profile_image']
        person = Person.objects.create(person_name=name,position=position,profile_image=profile)
        person.save()
        # image = request.POST['profile_image']
        # if 'file' in request.FILES:
        #     file = request.FILES['file']
        #     filename = file._name
        #
        #     fp = open('%s/%s' % (UPLOAD_DIR, filename) , 'wb')
        #     for chunk in file.chunks():
        #         fp.write(chunk)
        #         setattr(person,profile_image,chunk)
        #         person.save()
        #     fp.close()

        sk = dict(request.POST)['skill']
        degree = dict(request.POST)['skill_degree']
        number =0
        for s in sk  :
            skill = Skill.objects.create(devstack=s,person= person,degree=degree[number])
            skill.save()
            number+=1

        return HttpResponseRedirect(reverse('resume:detail', args=(person.id,)))
    else :
         return render(request,'resume_prac/resume_write.html')

def resume_detail(request,resume_id):
    person = Person.objects.get(id=resume_id)
    experience = person.experience_set.order_by('-startDate')
    return render(request,'resume_prac/resume_detail.html',{'person':person,'experience':experience})

def resume_search(request):
    if request.method =="GET":
        query = request.GET.get('q')
        person = Person.objects.filter(person_name__icontains=query)
        return render(request,'resume_prac/resume_list.html',{'resume_list':person})
