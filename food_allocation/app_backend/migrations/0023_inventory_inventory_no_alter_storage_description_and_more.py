# Generated by Django 4.2.5 on 2024-03-05 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0022_remove_storage_x_remove_storage_y_remove_storage_z'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='inventory_no',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storage',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.CreateModel(
            name='InventoryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('before', models.IntegerField()),
                ('after', models.IntegerField()),
                ('difference', models.IntegerField()),
                ('movement', models.CharField(choices=[('INBOUND', 'Inbound'), ('OUTBOUND', 'Outbound'), ('ADJUSTMENT', 'Adjustment')], max_length=50)),
                ('reason', models.CharField(blank=True, default='', max_length=200)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inventory_histories', to='app_backend.inventory')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
