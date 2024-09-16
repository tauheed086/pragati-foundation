# Generated by Django 5.1 on 2024-09-16 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0027_alter_volunteer_email_alter_volunteer_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='cause',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='heart_charity.cause'),
            preserve_default=False,
        ),
    ]
