# Generated by Django 4.2.7 on 2024-03-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdata', '0011_alter_customerdata_phone_alter_customerdata_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdata',
            name='pincode',
        ),
    ]
