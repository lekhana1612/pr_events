# Generated by Django 4.2.7 on 2023-12-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('eventdate', models.DateField(max_length=50)),
                ('eventname', models.CharField(max_length=50)),
                ('eventvenue', models.CharField(max_length=50)),
                ('eventcity', models.CharField(max_length=50)),
                ('quotation', models.CharField(max_length=50)),
                ('advance', models.CharField(max_length=50)),
                ('balance', models.CharField(max_length=50)),
            ],
        ),
    ]
