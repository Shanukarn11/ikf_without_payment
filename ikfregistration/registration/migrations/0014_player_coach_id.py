# Generated by Django 4.0.5 on 2022-06-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_coachmodel_barcode_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='coach_id',
            field=models.CharField(max_length=300, null=True),
        ),
    ]