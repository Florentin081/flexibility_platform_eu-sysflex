# Generated by Django 2.0.7 on 2020-03-31 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0004_flexibilitybid_power_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexibilitybid',
            name='direction',
            field=models.CharField(choices=[('plus', 'Up'), ('moins', 'Down')], max_length=10),
        ),
    ]
