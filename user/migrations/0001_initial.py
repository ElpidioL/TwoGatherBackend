# Generated by Django 4.2.5 on 2023-10-03 02:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Roles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('email', models.EmailField(max_length=128, verbose_name='E-mail')),
                ('photo', models.TextField(blank=True, null=True, verbose_name='Photo')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.CharField(choices=[(0, 'Inactive'), (1, 'Active')], max_length=255, verbose_name='Escritório base')),
                ('lastActive', models.DateTimeField()),
                ('isAdmin', models.BooleanField(default=False)),
                ('idRole', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.role')),
                ('messages', models.ManyToManyField(related_name='message', to='group.message', verbose_name='message')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ['name'],
            },
        ),
    ]
