# Generated by Django 3.1.2 on 2021-02-07 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210207_0844'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectEmployeeMapping',
        ),
    ]
