# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_prac', '0007_experience_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='ex_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
