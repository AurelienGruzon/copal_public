# Generated by Django 5.0.4 on 2024-10-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copal_manager', '0005_remove_contrat_numero_contrat'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='numero_contrat',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
