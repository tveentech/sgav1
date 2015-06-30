# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('work_telephone', models.CharField(max_length=255, blank=True)),
                ('residence_telephone', models.CharField(max_length=255, blank=True)),
                ('designation', models.CharField(max_length=255, blank=True)),
                ('email', models.EmailField(max_length=255)),
                ('alternate_email', models.TextField(blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('family_members', models.TextField(blank=True)),
                ('office_address', models.TextField(blank=True)),
                ('residential_address', models.TextField(blank=True)),
                ('reference', models.CharField(max_length=255, blank=True)),
                ('remarks', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='sgadata.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FloorLevelTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FloorPlanType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InternalRevisionVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('group', models.ForeignKey(blank=True, to='auth.Group', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RevisionVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, to='sgadata.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_type', models.CharField(default=b'UNPLANNED', max_length=255, choices=[(b'UNPLANNED', b'Unplanned'), (b'PLANEED', b'planned')])),
                ('drawing', models.CharField(max_length=255)),
                ('drawing_description', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('related_task', models.CharField(max_length=255, blank=True)),
                ('hours', models.CharField(max_length=255, blank=True)),
                ('scheduled_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('user_completed_date', models.DateTimeField(null=True, blank=True)),
                ('filelocation', models.CharField(max_length=255, blank=True)),
                ('reviewed', models.BooleanField(default=False)),
                ('completed_date', models.DateTimeField(null=True, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('filename_and_location_proper', models.BooleanField(default=False, help_text=b'Is Filename and Location Proper?', verbose_name=b'FileLocation?')),
                ('dispatched', models.BooleanField(default=False)),
                ('block', models.ForeignKey(to='sgadata.Block')),
                ('discipline', models.ForeignKey(to='sgadata.Discipline')),
                ('floor_level_tracker', models.ForeignKey(to='sgadata.FloorLevelTracker')),
                ('floor_plan_type', models.ForeignKey(to='sgadata.FloorPlanType')),
                ('internal_revision_version', models.ForeignKey(to='sgadata.InternalRevisionVersion')),
                ('phase', models.ForeignKey(to='sgadata.Phase')),
                ('project', models.ForeignKey(to='sgadata.Project')),
                ('revision_version', models.ForeignKey(to='sgadata.RevisionVersion')),
                ('stage', models.ForeignKey(to='sgadata.Stage')),
                ('task_master', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='phase',
            name='project',
            field=models.ForeignKey(to='sgadata.Project'),
        ),
        migrations.AddField(
            model_name='contact',
            name='project',
            field=models.ForeignKey(blank=True, to='sgadata.Project', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='subcategory',
            field=models.ForeignKey(blank=True, to='sgadata.SubCategory', null=True),
        ),
        migrations.AddField(
            model_name='block',
            name='project',
            field=models.ForeignKey(to='sgadata.Project'),
        ),
    ]
