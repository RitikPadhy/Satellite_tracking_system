# Generated by Django 4.2.11 on 2024-05-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaunchCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=100)),
                ('object_id', models.CharField(max_length=100)),
                ('epoch', models.DateTimeField()),
                ('mean_motion', models.FloatField()),
                ('eccentricity', models.FloatField()),
                ('inclination', models.FloatField()),
                ('ra_of_asc_node', models.FloatField()),
                ('arg_of_pericenter', models.FloatField()),
                ('mean_anomaly', models.FloatField()),
                ('ephemeris_type', models.IntegerField()),
                ('classification_type', models.CharField(max_length=1)),
                ('norad_cat_id', models.IntegerField()),
                ('element_set_no', models.IntegerField()),
                ('rev_at_epoch', models.IntegerField()),
                ('bstar', models.FloatField()),
                ('mean_motion_dot', models.FloatField()),
                ('mean_motion_ddot', models.FloatField()),
            ],
        ),
    ]
