from django.contrib import admin
from .models import Person,Skill,Experience,Tag

# Register your models here.


admin.site.register(Person)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Tag)
