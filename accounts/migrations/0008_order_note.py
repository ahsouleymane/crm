# Generated by Django 3.2.12 on 2022-07-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
