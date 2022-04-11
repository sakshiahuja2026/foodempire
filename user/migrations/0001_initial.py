# Generated by Django 4.0.2 on 2022-04-07 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('Date', models.DateField(default=datetime.datetime.utcnow)),
                ('Time', models.TimeField()),
                ('Number', models.IntegerField()),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
    ]