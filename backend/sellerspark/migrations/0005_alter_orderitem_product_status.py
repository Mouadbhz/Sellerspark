# Generated by Django 5.0.3 on 2024-05-21 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerspark', '0004_alter_orderitem_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product_status',
            field=models.CharField(choices=[('processing', 'Processing'), ('vendor cancel', 'Vendor Cancel'), ('delivered', 'Delivered'), ('client cancel', 'Client Cancel')], default='processing', max_length=30),
        ),
    ]
