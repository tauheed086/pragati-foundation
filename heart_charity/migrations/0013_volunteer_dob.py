# Generated by Django 5.1 on 2024-09-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0012_remove_volunteer_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]