# Generated by Django 4.0.5 on 2022-07-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_merge_20220630_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position1',
            field=models.CharField(default='', max_length=50, verbose_name='Position given'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.CharField(default='', max_length=5),
        ),
    ]
