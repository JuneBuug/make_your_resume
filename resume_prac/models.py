from django.db import models
import json

# Create your models here.


class Person(models.Model) :
	person_name = models.CharField(max_length=80)
	position = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to='%Y/%m/%d/orig',default='default.png')
	person_desc = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.person_name

class Skill(models.Model) :
	devstack = models.CharField(max_length=80)
	degree = models.IntegerField(default=0)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)

	def __str__(self):
		return self.devstack

DEFAULT_PERSON_ID = 1
class Experience(models.Model) :
	startDate = models.DateTimeField(blank=True)
	endDate = models.DateTimeField(blank=True)
	ex_name = models.CharField(max_length=120)
	ex_desc = models.TextField(blank=True, null=True) # 경험/경력에 대한 설명
	person = models.ForeignKey('Person', on_delete=models.CASCADE, default=DEFAULT_PERSON_ID)

	def __str__(self):
		return self.ex_name
