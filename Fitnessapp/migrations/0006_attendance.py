# Generated by Django 4.1.5 on 2023-01-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitnessapp', '0005_membershipplan_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('login', models.CharField(max_length=50)),
                ('logout', models.CharField(max_length=50)),
                ('workout', models.CharField(max_length=100)),
                ('trainer', models.CharField(max_length=100)),
            ],
        ),
    ]
