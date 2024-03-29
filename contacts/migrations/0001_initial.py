# Generated by Django 2.2.7 on 2019-11-17 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 17, 16, 17, 48, 944204))),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
