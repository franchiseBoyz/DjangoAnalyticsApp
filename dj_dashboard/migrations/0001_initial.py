# Generated by Django 4.0.4 on 2022-05-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=50)),
                ('shipping_cost', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]