# Generated by Django 5.0.4 on 2024-04-22 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employee_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone_number',
        ),
    ]
