# Generated by Django 4.1.3 on 2024-05-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_rename_nombre_menu_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='descripcion',
            field=models.CharField(max_length=2000),
        ),
    ]
