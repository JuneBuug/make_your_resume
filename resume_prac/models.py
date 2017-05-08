from django.db import models
import json

# Create your models here.


class Person(models.Model) :
	person_name = models.CharField(max_length=80)
	position = models.CharField(max_length=200)
	profile_image = models.ImageField(upload_to='%Y/%m/%d/orig',default='default.png')

	def __str__(self):
		return self.person_name

class Skill(models.Model) :
	devstack = models.CharField(max_length=80)
	degree = models.IntegerField(default=0)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)

	def __str__(self):
		return self.devstack
