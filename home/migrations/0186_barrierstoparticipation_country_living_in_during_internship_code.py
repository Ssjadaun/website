# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-21 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0185_auto_20200819_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrierstoparticipation',
            name='country_living_in_during_internship_code',
            field=models.CharField(blank=True, max_length=2, verbose_name='ISO 3166-1 alpha-2 country code'),
        ),
    ]
