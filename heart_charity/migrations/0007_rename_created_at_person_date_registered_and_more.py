# Generated by Django 5.1 on 2024-09-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0006_rename_date_registered_person_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='created_at',
            new_name='date_registered',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='aadhaar_no',
        ),
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.RemoveField(
            model_name='person',
            name='dependent',
        ),
        migrations.RemoveField(
            model_name='person',
            name='dis_percentage',
        ),
        migrations.RemoveField(
            model_name='person',
            name='disability_type',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='person',
            name='it_return',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='person',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='person',
            name='udid_no',
        ),
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
