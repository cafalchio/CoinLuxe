# Generated by Django 3.2.19 on 2023-06-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_backend', '0009_auto_20230614_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='blockchain_site',
            field=models.JSONField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coins',
            name='categories',
            field=models.JSONField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coins',
            name='homepage',
            field=models.JSONField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coins',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coins',
            name='symbol',
            field=models.CharField(max_length=100),
        ),
    ]