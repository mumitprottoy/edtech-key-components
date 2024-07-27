# Generated by Django 5.0.6 on 2024-07-18 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0007_rename_meta_appearance_metadata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='admission_test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='qb.admissiontest'),
        ),
    ]