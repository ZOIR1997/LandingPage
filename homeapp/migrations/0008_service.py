# Generated by Django 4.1.1 on 2022-10-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('programming', models.CharField(max_length=50)),
                ('information', models.TextField()),
            ],
        ),
    ]
