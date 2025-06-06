# Generated by Django 4.2.9 on 2025-05-17 19:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_medication_frequency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medication',
            options={},
        ),
        migrations.AlterField(
            model_name='medication',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
