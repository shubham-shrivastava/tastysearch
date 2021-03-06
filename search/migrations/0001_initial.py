# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(max_length=200)),
                ('userId', models.CharField(max_length=200)),
                ('profileName', models.CharField(max_length=200)),
                ('helpfulness', models.CharField(max_length=200)),
                ('score', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=20000)),
                ('text', models.CharField(max_length=20000)),
            ],
        ),
    ]
