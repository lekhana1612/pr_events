# Generated by Django 4.2.7 on 2024-03-01 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_decoration_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='decoration',
            name='image',
        ),
        migrations.AddField(
            model_name='decoration',
            name='option',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
