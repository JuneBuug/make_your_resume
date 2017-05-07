from django.db import models
import json

# Create your models here.


class Person(models.Model) :
	person_name = models.CharField(max_length=80)
	position = models.CharField(max_length=200)

	def __str__(self):
		return "%s (%s)" % (person_name,position)

class Skill(models.Model) :
	devstack = models.CharField(max_length=80)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)

	def __str__(self):
		return self.devstack