# Generated by Django 2.0.7 on 2020-11-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prequalification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gridimpactassessmentinput',
            name='direction',
            field=models.CharField(choices=[('+', 'Up'), ('-', 'Down')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
