# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-13 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0013_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Foodtype',
        ),
        migrations.DeleteModel(
            name='Mainshow',
        ),
        migrations.DeleteModel(
            name='Mustbuy',
        ),
        migrations.DeleteModel(
            name='Nav',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='Wheel',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
