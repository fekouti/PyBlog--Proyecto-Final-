# Generated by Django 4.0.6 on 2022-08-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUsers', '0002_users_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=140, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
