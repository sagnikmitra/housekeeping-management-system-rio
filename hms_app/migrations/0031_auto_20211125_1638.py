# Generated by Django 3.2.6 on 2021-11-25 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0030_auto_20211125_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_details',
            name='room_housekeeper_note',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Monthly_roster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_from', models.CharField(max_length=15)),
                ('date_to', models.CharField(max_length=15)),
                ('time_from', models.CharField(max_length=15)),
                ('time_to', models.CharField(max_length=15)),
                ('update_time', models.CharField(max_length=15)),
                ('update_by', models.CharField(max_length=25)),
                ('staff_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hms_app.staff')),
                ('staff_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hms_app.staff_type')),
            ],
        ),
    ]
