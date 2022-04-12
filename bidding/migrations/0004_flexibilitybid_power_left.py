# Generated by Django 2.0.7 on 2020-03-31 03:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_auto_20200326_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexibilitybid',
            name='power_left',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
            preserve_default=False,
        ),
    ]
