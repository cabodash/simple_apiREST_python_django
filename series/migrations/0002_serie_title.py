# Generated by Django 5.0.1 on 2024-02-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]