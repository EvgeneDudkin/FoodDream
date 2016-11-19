# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_title', models.CharField(max_length=200)),
                ('answer_status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_title', models.CharField(max_length=200)),
                ('request_requester', models.CharField(max_length=20)),
                ('request_status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'request',
            },
        ),
    ]
