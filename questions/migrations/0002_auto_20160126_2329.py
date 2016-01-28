# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=9, primary_key=True, serialize=False, unique=True),
        ),
    ]