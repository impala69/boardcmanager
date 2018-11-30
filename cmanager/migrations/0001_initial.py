# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-09 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrt_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('card_number', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('year_of_birth', models.IntegerField()),
                ('month_of_birth', models.IntegerField()),
                ('day_of_birth', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmanager.User'),
        ),
    ]