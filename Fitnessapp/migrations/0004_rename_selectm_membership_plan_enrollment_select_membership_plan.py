# Generated by Django 4.1.5 on 2023-01-26 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fitnessapp', '0003_rename_phonen_number_enrollment_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='selectM_membership_plan',
            new_name='select_membership_plan',
        ),
    ]
