# Generated by Django 3.1.2 on 2021-02-04 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210204_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='employee.employee'),
        ),
    ]
