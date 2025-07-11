# Generated by Django 4.2.5 on 2024-03-26 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0030_alter_family_name_alter_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('package_no', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('CANCELLED', 'Cancelled'), ('PACKED', 'Packed')], max_length=20)),
                ('allocation_family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='packages', to='app_backend.allocationfamily')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='packages', to='app_backend.family')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PackageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(choices=[('NEW', 'New'), ('CANCELLED', 'Cancelled'), ('PACKED', 'Packed')], max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_histories', to='app_backend.package')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_items', to='app_backend.inventory')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_items', to='app_backend.package')),
            ],
            options={
                'unique_together': {('package', 'inventory')},
            },
        ),
    ]
