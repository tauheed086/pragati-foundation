# Generated by Django 5.1 on 2024-09-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0028_donations_cause'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='cause',
        ),
        migrations.AddField(
            model_name='person',
            name='failed_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='otp_created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]