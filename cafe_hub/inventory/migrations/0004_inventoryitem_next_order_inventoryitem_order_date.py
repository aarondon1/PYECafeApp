# Generated by Django 5.1 on 2024-08-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_user_inventoryitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='next_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='order_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
