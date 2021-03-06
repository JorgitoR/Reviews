# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-18 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(help_text='ID de objeto revisado')),
                ('score', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Puntuaci\xf3n entera en un rango de 1 a  5')),
                ('comment', models.TextField(blank=True, help_text='Un comentario explicando el resultado de la revision', max_length=1000)),
                ('anonymous', models.BooleanField(default=False, help_text='Mantenga la identidad del revisor anonima')),
                ('comment_approved', models.BooleanField(default=True, help_text='The comment has been approved by an admin')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date and time last modified')),
                ('content_type', models.ForeignKey(help_text='Modelo de objeto revisado', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
