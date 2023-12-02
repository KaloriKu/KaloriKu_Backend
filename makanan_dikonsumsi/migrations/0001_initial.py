# Generated by Django 4.2.7 on 2023-12-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('makanan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MakananDikonsumsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('makanan', models.ManyToManyField(to='makanan.makanan')),
            ],
        ),
    ]
