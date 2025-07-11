# Generated by Django 5.0.3 on 2024-03-30 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0031_package_packagehistory_packageitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='allocation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='packages', to='app_backend.allocation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('CANCELLED', 'Cancelled'), ('PACKED', 'Packed'), ('DELIVERED', 'Delivered')], max_length=20),
        ),
        migrations.AlterField(
            model_name='packagehistory',
            name='action',
            field=models.CharField(choices=[('NEW', 'New'), ('CANCELLED', 'Cancelled'), ('PACKED', 'Packed'), ('DELIVERED', 'Delivered')], max_length=50),
        ),
    ]
