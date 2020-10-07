# Generated by Django 3.0.8 on 2020-09-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_product_instock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]