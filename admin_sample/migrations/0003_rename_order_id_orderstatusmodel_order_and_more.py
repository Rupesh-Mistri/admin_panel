# Generated by Django 5.0.7 on 2024-11-18 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_sample', '0002_orderstatusmodel_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderstatusmodel',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderstatusmodel',
            old_name='seller_id',
            new_name='seller',
        ),
        migrations.RenameField(
            model_name='orderstatusmodel',
            old_name='user_id',
            new_name='user',
        ),
    ]