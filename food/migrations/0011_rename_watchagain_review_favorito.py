# Generated by Django 4.1.3 on 2024-05-22 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_review_calificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='watchAgain',
            new_name='favorito',
        ),
    ]
