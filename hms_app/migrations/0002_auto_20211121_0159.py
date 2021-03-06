# Generated by Django 3.2.6 on 2021-11-20 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_details',
            name='room_inspect_status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Housekeeper_room_visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('housekeeper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_app.housekeeper')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_app.room')),
            ],
        ),
        migrations.CreateModel(
            name='Housekeeper_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('housekeeper_status', models.CharField(max_length=20)),
                ('housekeeper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_app.housekeeper')),
            ],
        ),
    ]
