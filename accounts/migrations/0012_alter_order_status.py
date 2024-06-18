# Generated by Django 5.0.6 on 2024-06-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('En attente', 'En_attente'), ('En cours de livraison', 'En_cours_de_livraison'), ('Livré', 'LivrE')], max_length=200, null=True),
        ),
    ]