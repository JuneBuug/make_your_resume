from django.shortcuts import render
from .models import Person
from .models import Skill
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def resume_list(request):
    resume_list = Person.objects.all()
    return render(request,'resume_prac/resume_list.html',{'resume_list':resume_list})

def resume_write(request):

    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        skill = request.POST['skill']
        person = Person.objects.create(person_name=name,position=position)
        person.save()
        skill = Skill.objects.create(devstack=skill,person= person)
        skill.save()
        # return HttpResponseRedirect(reverse()'/resume/'+str(person.id))
        return HttpResponseRedirect(reverse('resume:detail', args=(person.id,)))
    else :
         return render(request,'resume_prac/resume_write.html')

def resume_detail(request,resume_id):
    person = Person.objects.get(id=resume_id)
    return render(request,'resume_prac/resume_detail.html',{'person':person})
