# Generated by Django 3.2.6 on 2021-11-26 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0031_auto_20211125_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_app.room_floor'),
        ),
    ]
