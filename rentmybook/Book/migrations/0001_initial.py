# Generated by Django 3.0.5 on 2020-04-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('sno', models.CharField(max_length=200)),
                ('book_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('tag_code', models.CharField(max_length=50)),
                ('user_image', models.ImageField(upload_to='images/')),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=200)),
                ('user_id_supplier', models.CharField(max_length=200)),
                ('current_user', models.CharField(max_length=100)),
                ('date_of_rent', models.DateTimeField(auto_now_add=True)),
                ('rental_due', models.FloatField(max_length=200)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('fine_per_day', models.IntegerField()),
                ('Deposit_by_renter', models.IntegerField()),
            ],
        ),
    ]
