# Generated by Django 2.1.15 on 2022-04-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('property_class', models.CharField(max_length=20)),
                ('property_type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('features', models.CharField(max_length=500)),
                ('no_bedrooms', models.IntegerField()),
                ('no_bathrooms', models.IntegerField()),
                ('property_map', models.CharField(max_length=100)),
                ('ber_rating', models.CharField(max_length=2)),
                ('photos', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
