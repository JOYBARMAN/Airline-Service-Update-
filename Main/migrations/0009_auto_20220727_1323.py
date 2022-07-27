# Generated by Django 3.2.9 on 2022-07-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_flight_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='adult',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='child',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='date2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='fclass',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
