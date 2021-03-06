# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-09 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0011_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(default='axf.png', max_length=40)),
                ('rank', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
