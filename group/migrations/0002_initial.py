# Generated by Django 4.2.5 on 2023-10-03 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='idSentBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user'),
        ),
        migrations.AddField(
            model_name='message',
            name='readBy',
            field=models.ManyToManyField(related_name='readBy', to='user.user', verbose_name='Read By'),
        ),
        migrations.AddField(
            model_name='group',
            name='idAdmin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user'),
        ),
        migrations.AddField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to='user.user', verbose_name='participants'),
        ),
    ]