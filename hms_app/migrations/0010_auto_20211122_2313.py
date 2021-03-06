# Generated by Django 3.2.6 on 2021-11-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0009_alter_housekeeper_details_housekeeper_room_visit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housekeeper_details',
            name='housekeeper_room_visit',
        ),
        migrations.CreateModel(
            name='Housekeeper_room_visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('housekeeper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_app.housekeeper')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_app.room')),
            ],
        ),
    ]
