# Generated by Django 3.0.8 on 2020-08-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_productsize_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]