# Generated by Django 4.0 on 2024-11-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='furniture_images/'),
        ),
    ]
