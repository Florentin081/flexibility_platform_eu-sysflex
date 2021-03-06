# Generated by Django 2.0.7 on 2020-04-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0002_flexibilityactivationorder_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexibilityactivationorder',
            name='direction',
            field=models.CharField(choices=[('+', 'Up'), ('-', 'Down')], max_length=10),
        ),
        migrations.AlterField(
            model_name='flexibilityactivationrequest',
            name='direction',
            field=models.CharField(choices=[('+', 'Up'), ('-', 'Down')], max_length=10),
        ),
    ]
