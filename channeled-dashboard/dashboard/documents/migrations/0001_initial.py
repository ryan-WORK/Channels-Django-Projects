# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 11:59
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=767, verbose_name='title')),
                ('slug', models.SlugField(max_length=767, unique=True, verbose_name='slug')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='image')),
                ('abstract', ckeditor.fields.RichTextField(null=True, verbose_name='abstract')),
                ('text', ckeditor.fields.RichTextField(null=True, verbose_name='content')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
    ]