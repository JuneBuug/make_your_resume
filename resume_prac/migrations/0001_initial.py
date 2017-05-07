# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=80)),
                ('position', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devstack', models.CharField(max_length=80)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_prac.Person')),
            ],
        ),
    ]