# Generated by Django 3.0.8 on 2020-08-28 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_variation_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product'),
        ),
    ]
