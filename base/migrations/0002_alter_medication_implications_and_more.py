# Generated by Django 4.2.3 on 2023-11-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='implications',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='medication',
            name='intention',
            field=models.CharField(max_length=200),
        ),
    ]
