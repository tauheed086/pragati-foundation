# Generated by Django 5.1 on 2024-10-14 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0037_contact_phone_alter_person_aadhaar_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]