# Generated by Django 4.2.7 on 2024-02-14 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdata', '0002_alter_customerdata_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdata',
            old_name='id',
            new_name='customer_id',
        ),
    ]
