# Generated by Django 3.2.6 on 2021-11-22 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0012_auto_20211123_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_details',
            name='room_updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_app.staff'),
        ),
    ]
