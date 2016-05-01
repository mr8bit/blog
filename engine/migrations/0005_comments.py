# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 22:36
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20160501_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('email', models.EmailField(max_length=200)),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Комментарий')),
                ('ip', models.CharField(default=' ', max_length=100)),
                ('anser_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='engine.Comments')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Article')),
            ],
            options={
                'db_table': 'comments',
                'ordering': ['-time'],
            },
        ),
    ]
