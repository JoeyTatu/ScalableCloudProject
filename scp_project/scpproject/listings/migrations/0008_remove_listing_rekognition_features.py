# Generated by Django 2.1.15 on 2022-04-29 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20220429_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='rekognition_features',
        ),
    ]
