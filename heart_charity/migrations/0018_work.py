# Generated by Django 5.1 on 2024-09-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0017_alter_person_dependent'),
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='')),
                ('detail', models.CharField(max_length=500)),
                ('raised', models.FloatField()),
                ('goal', models.FloatField()),
            ],
        ),
    ]
