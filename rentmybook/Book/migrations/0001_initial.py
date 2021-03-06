# Generated by Django 3.0.5 on 2020-05-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('book_image', models.ImageField(upload_to='image/')),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=200)),
                ('owner_user_id', models.CharField(max_length=200)),
                ('current_user_id', models.CharField(max_length=100)),
                ('date_of_rent', models.DateTimeField(auto_now_add=True)),
                ('rental_due', models.FloatField(max_length=201)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('fine_per_day', models.IntegerField()),
                ('deposit_by_renter', models.IntegerField()),
            ],
            options={
                'db_table': 'BOOK',
            },
        ),
    ]
