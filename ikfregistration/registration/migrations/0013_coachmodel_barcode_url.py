# Generated by Django 4.0.5 on 2022-06-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_alter_coachmodel_academy_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachmodel',
            name='barcode_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
