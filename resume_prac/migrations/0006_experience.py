# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_prac', '0005_auto_20170508_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField(blank=True)),
                ('endDate', models.DateTimeField(blank=True)),
                ('ex_name', models.CharField(max_length=120)),
                ('ex_desc', models.CharField(max_length=900)),
            ],
        ),
    ]
