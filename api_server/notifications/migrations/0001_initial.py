# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.TextField(default='No title')),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StartUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('start_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.StartUrl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='starturl',
            name='user',
            field=models.ManyToManyField(through='notifications.UserWeb', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newsnotification',
            name='start_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.StartUrl'),
        ),
        migrations.AlterUniqueTogether(
            name='userweb',
            unique_together=set([('user', 'start_url')]),
        ),
    ]
