# Generated by Django 3.0.5 on 2020-05-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='deposit_by_renter',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='fine_per_day',
            field=models.CharField(max_length=50),
        ),
    ]