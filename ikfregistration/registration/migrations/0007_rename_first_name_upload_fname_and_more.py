# Generated by Django 4.0.5 on 2022-06-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_upload_first_name_upload_last_name_upload_mobile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='upload',
            old_name='last_name',
            new_name='lname',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='fname',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='lname',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
