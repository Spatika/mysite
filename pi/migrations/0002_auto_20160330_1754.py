# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 09:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputfeatures',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='Events',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='Followers',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='Friends',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='Groups',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='Likes',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='a_score',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='c_score',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='curr_location',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='e_score',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='es_score',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='fb_degree',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='o_score',
        ),
        migrations.RemoveField(
            model_name='inputfeatures',
            name='photos_tagged_in',
        ),
    ]
