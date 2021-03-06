# Generated by Django 2.0.7 on 2020-10-26 09:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flexibility_platform', '0007_product_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexibilityNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_indicative_power_needed', models.DecimalField(decimal_places=3, default='0.1', max_digits=10)),
                ('preparation_period', models.PositiveIntegerField()),
                ('localization_factor', models.TextField(blank=True, null=True)),
                ('expiration_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needproduct', to='flexibility_platform.Product')),
                ('system_operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flexibility_platform.SystemOperator')),
            ],
        ),
        migrations.CreateModel(
            name='FlexibilityNeedAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability_start', models.DateTimeField()),
                ('availability_end', models.DateTimeField()),
                ('flexibility_need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='need_availabilitys', to='prequalification.FlexibilityNeed')),
            ],
        ),
        migrations.CreateModel(
            name='FlexibilityPotential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.DecimalField(decimal_places=3, max_digits=11, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('power_constraint', models.DecimalField(blank=True, decimal_places=3, max_digits=11, null=True, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('preparation_period', models.PositiveIntegerField()),
                ('compliance_demonstration', models.TextField()),
                ('localization_factor', models.TextField(blank=True, null=True)),
                ('metering_point_id', models.TextField()),
                ('baseline_type', models.TextField()),
                ('expiration_date', models.DateTimeField()),
                ('is_prequalified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fsp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flexibility_platform.FlexibilityServiceProvider')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='potentialproduct', to='flexibility_platform.Product')),
            ],
        ),
        migrations.CreateModel(
            name='FlexibilityPotentialAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability_start', models.DateTimeField()),
                ('availability_end', models.DateTimeField()),
                ('flexibility_potential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='potential_availabilitys', to='prequalification.FlexibilityPotential')),
            ],
        ),
        migrations.CreateModel(
            name='GridImpactAssessmentInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=11)),
                ('location', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('potential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prequalification.FlexibilityPotential')),
                ('system_operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flexibility_platform.SystemOperator')),
            ],
        ),
        migrations.CreateModel(
            name='GridImpactAssessmentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('potential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prequalification.FlexibilityPotential')),
                ('system_operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flexibility_platform.SystemOperator')),
            ],
        ),
        migrations.CreateModel(
            name='PrequalificationInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_prequalification_product', models.TextField()),
                ('status_grid_impact', models.TextField()),
                ('commentary', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flexibility_potential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='potential_need_prequalified', to='prequalification.FlexibilityPotential')),
            ],
        ),
    ]
