# Generated by Django 4.2.6 on 2023-10-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_information_text_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_fa',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]