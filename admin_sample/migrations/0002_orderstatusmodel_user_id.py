# Generated by Django 5.0.7 on 2024-11-18 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatusmodel',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_sample.userdetailsmodel'),
            preserve_default=False,
        ),
    ]