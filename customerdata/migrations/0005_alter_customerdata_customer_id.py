# Generated by Django 4.2.7 on 2024-02-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerdata', '0004_alter_customerdata_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdata',
            name='customer_id',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
