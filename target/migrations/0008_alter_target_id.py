# Generated by Django 4.2.7 on 2023-12-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0007_alter_target_perubahanberatbadan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]