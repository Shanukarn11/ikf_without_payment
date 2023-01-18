# Generated by Django 4.0.4 on 2022-06-14 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_mastercoachlabels'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterDateLimit',
            fields=[
                ('id', models.CharField(db_index=True, max_length=150, primary_key=True, serialize=False)),
                ('lowerlimit', models.DateField(db_index=True)),
                ('upperlimit', models.DateField(db_index=True)),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.masterseason', verbose_name='master_season_id_limit')),
            ],
        ),
    ]
