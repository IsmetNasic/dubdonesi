# Generated by Django 3.0.8 on 2020-08-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_variation_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='size',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]