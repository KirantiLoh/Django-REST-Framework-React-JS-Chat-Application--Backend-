# Generated by Django 3.2.9 on 2021-11-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_profile_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='room',
            field=models.ManyToManyField(related_name='rooms', to='api.Room'),
        ),
    ]
