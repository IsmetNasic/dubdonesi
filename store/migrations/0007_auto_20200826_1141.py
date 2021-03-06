# Generated by Django 3.0.8 on 2020-08-26 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_productsize_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('size', 'size'), ('#', '#'), ('#', '#')], default='size', max_length=120)),
                ('title', models.CharField(max_length=120, null=True)),
                ('price', models.FloatField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
    ]
