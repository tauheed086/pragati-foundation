# Generated by Django 5.1 on 2024-09-05 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0011_alter_volunteer_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='dob',
        ),
    ]
