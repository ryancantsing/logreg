# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0004_auto_20171222_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='users_poked',
        ),
        migrations.AddField(
            model_name='users',
            name='times_poked',
            field=models.ManyToManyField(related_name='_users_times_poked_+', to='login_reg.Users'),
        ),
    ]