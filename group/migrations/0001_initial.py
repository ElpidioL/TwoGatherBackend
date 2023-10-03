# Generated by Django 4.2.5 on 2023-10-03 02:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('photo', models.TextField(blank=True, null=True, verbose_name='Photo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('isTransmission', models.BooleanField(default=False, verbose_name='Transmission')),
                ('isPrivate', models.BooleanField(default=True, verbose_name='Private')),
                ('archive', models.BooleanField(default=False, verbose_name='Archived')),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sent date')),
                ('priority', models.CharField(choices=[(0, 'Normal'), (1, 'Urgent')], max_length=255, verbose_name='Priority')),
                ('idGroup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='group.group')),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'ordering': ['-date'],
            },
        ),
    ]