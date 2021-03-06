# Generated by Django 2.0.7 on 2020-05-10 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0007_auto_20200510_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verification',
            name='flexibility_activation_order',
        ),
        migrations.RemoveField(
            model_name='verification',
            name='flexibility_activation_request',
        ),
        migrations.RemoveField(
            model_name='verification',
            name='flexibility_service_provider',
        ),
        migrations.AlterField(
            model_name='flexibilityactivationorder',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='activation.FlexibilityActivationRequest'),
        ),
        migrations.DeleteModel(
            name='Verification',
        ),
    ]
