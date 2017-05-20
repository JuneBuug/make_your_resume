from django.db import models
import json

# Create your models here.


class Person(models.Model) :
	person_name = models.CharField(max_length=80)
	position = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to='%Y/%m/%d/orig',default='default.png')
	person_desc = models.TextField(blank=True, null=True)
	person_oneline = models.CharField(max_length=80, blank=True, null=True)
	tag_set = models.ManyToManyField('Tag',blank=True)

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
	startDate = models.DateField(blank=True)
	endDate = models.DateField(blank=True)
	ex_name = models.CharField(max_length=120)
	ex_desc = models.TextField(blank=True, null=True) # 경험/경력에 대한 설명
	person = models.ForeignKey('Person', on_delete=models.CASCADE, default=DEFAULT_PERSON_ID)

	def __str__(self):
		return self.ex_name

class Tag(models.Model) :
	tag_name = models.CharField(max_length=120)

	def __str__(self):
		return self.tag_name
