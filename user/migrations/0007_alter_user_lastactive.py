# Generated by Django 4.2.6 on 2023-10-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_date_joined_user_first_name_user_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lastActive',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]