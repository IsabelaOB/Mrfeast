# Generated by Django 4.1.3 on 2024-05-22 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_rename_watchagain_review_favorito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='calificacion',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
