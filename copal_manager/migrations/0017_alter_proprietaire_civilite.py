# Generated by Django 5.0.4 on 2024-12-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copal_manager', '0016_alter_bienimmobilier_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proprietaire',
            name='civilite',
            field=models.CharField(choices=[('M', 'Monsieur'), ('Mme', 'Madame'), ('M&Mme', 'Monsieur et Madame'), ('Societe', 'Societe')], default='M', max_length=20),
        ),
    ]
