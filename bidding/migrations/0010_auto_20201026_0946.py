# Generated by Django 2.0.7 on 2020-10-26 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0009_auto_20200428_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callfortenders',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='flexibilitybid',
            name='direction',
        ),
    ]
