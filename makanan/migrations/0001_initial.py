# Generated by Django 4.2.7 on 2023-11-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('nama', models.CharField()),
                ('jumlahKalori', models.FloatField()),
                ('jumlahLemak', models.FloatField()),
                ('jumlahKarbohidrat', models.FloatField()),
                ('jumlahProtein', models.FloatField()),
            ],
        ),
    ]
