# Generated by Django 4.2.7 on 2023-12-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0008_alter_target_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='target',
            name='perubahanBeratBadan',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
