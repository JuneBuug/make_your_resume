# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_prac', '0003_person_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='%Y/%m/%d/orig'),
        ),
    ]
