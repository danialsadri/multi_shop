# Generated by Django 4.2.6 on 2023-10-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_discountcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
