# Generated by Django 4.1.1 on 2022-09-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_alter_about_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programm', models.CharField(max_length=50)),
                ('progress', models.CharField(max_length=10)),
            ],
        ),
    ]
