# Generated by Django 3.0.8 on 2020-08-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
