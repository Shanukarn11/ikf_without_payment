# Generated by Django 4.0.5 on 2022-06-11 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_masterpartner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mastercategory',
            options={'verbose_name': 'Master Category', 'verbose_name_plural': 'Master Categories'},
        ),
        migrations.AlterModelOptions(
            name='mastercity',
            options={'verbose_name': 'Master City', 'verbose_name_plural': 'Master Cities'},
        ),
        migrations.AlterModelOptions(
            name='mastergroupcity',
            options={'verbose_name': 'Master Group City', 'verbose_name_plural': 'Master Group Cities'},
        ),
        migrations.AlterModelOptions(
            name='masterlabels',
            options={'verbose_name': 'Master Label', 'verbose_name_plural': 'Master Labels'},
        ),
        migrations.AlterModelOptions(
            name='masterroles',
            options={'verbose_name': 'Master Role', 'verbose_name_plural': 'Master Roles'},
        ),
    ]
