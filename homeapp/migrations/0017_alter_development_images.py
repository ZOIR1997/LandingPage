# Generated by Django 4.1.1 on 2022-10-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0016_development_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='development',
            name='images',
            field=models.ImageField(null=True, upload_to='images_programming/'),
        ),
    ]
