# Generated by Django 3.2.6 on 2021-11-22 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0006_auto_20211122_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='housekeeper_details',
            name='housekeeper_room_visit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hms_app.housekeeper_room_visit'),
            preserve_default=False,
        ),
    ]
