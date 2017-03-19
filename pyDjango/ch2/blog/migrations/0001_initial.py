# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias', unique=True, verbose_name='SLUG')),
                ('description', models.CharField(blank=True, help_text='simple description text', max_length=100, verbose_name='DESCRIPTION')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
            ],
            options={
                'verbose_name': 'post',
                'ordering': ('-modify_date',),
                'verbose_name_plural': 'posts',
                'db_table': 'my_post',
            },
        ),
    ]
