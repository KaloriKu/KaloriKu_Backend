# Generated by Django 4.2.7 on 2023-12-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='berat_badan',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='registereduser',
            name='tinggi_badan',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
