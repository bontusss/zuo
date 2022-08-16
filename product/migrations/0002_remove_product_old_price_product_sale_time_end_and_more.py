# Generated by Django 4.0.6 on 2022-07-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='old_price',
        ),
        migrations.AddField(
            model_name='product',
            name='sale_time_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_time_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
