# Generated by Django 5.0.6 on 2024-07-14 04:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0002_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_appeared', models.BooleanField(default=False)),
                ('has_passage', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qb.chapter')),
            ],
        ),
        migrations.AlterField(
            model_name='appearance',
            name='meta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qb.questionmetadata'),
        ),
        migrations.AlterField(
            model_name='passage',
            name='meta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qb.questionmetadata'),
        ),
        migrations.AlterField(
            model_name='question',
            name='meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qb.questionmetadata'),
        ),
    ]