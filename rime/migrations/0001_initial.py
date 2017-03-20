# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-20 03:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(default='INIT', max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('appliance', models.CharField(max_length=2048)),
                ('site', models.CharField(max_length=2048)),
                ('implementation', models.CharField(max_length=2048)),
                ('remote_id', models.CharField(max_length=2048)),
                ('remote_status', models.CharField(default='NONE', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=2048)),
                ('credentials', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hints', models.TextField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rime.Cluster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cluster',
            name='credential',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rime.Credential'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='root_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clusters', to=settings.AUTH_USER_MODEL),
        ),
    ]
