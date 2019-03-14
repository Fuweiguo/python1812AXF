# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-13 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0015_auto_20190313_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('identifier', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.User')),
            ],
            options={
                'db_table': 'axf_order',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Order')),
            ],
            options={
                'db_table': 'axf_ordergoods',
            },
        ),
    ]
