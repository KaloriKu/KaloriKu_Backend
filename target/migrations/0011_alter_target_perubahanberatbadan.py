# Generated by Django 4.2.7 on 2023-12-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0010_alter_target_perubahanberatbadan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='perubahanBeratBadan',
            field=models.IntegerField(default=0),
        ),
    ]
