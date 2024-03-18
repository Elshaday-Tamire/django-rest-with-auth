# Generated by Django 5.0.3 on 2024-03-18 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EqubType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equb_Type_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equb_name', models.CharField(max_length=100)),
                ('equb_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equb.equbtype')),
            ],
        ),
    ]