# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import fileupload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SingleUseToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=fileupload.models.get_new_token, max_length=200)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='token',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='fileupload.SingleUseToken'),
        ),
    ]
