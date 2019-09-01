# Generated by Django 2.1.7 on 2019-08-31 13:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('closed_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('number', models.CharField(blank=True, max_length=30, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(blank=True, max_length=50, null=True)),
                ('gateway', models.CharField(blank=True, max_length=60, null=True)),
                ('test', models.BooleanField(default=False)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('subtotal_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('total_weight', models.IntegerField(blank=True, null=True)),
                ('total_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('taxes_included', models.BooleanField(default=False)),
                ('currency', models.CharField(blank=True, max_length=4, null=True)),
                ('financial_status', models.CharField(blank=True, max_length=20, null=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('total_discounts', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('total_line_items_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('cart_token', models.CharField(blank=True, max_length=50, null=True)),
                ('buyer_accepts_marketing', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('referring_site', models.URLField(blank=True, null=True)),
                ('landing_site', models.URLField(blank=True, null=True)),
                ('cancelled_at', models.DateTimeField()),
                ('cancel_reason', models.CharField(blank=True, max_length=20, null=True)),
                ('total_price_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('checkout_token', models.CharField(blank=True, max_length=50, null=True)),
                ('reference', models.CharField(blank=True, max_length=150, null=True)),
                ('user_id', models.CharField(blank=True, max_length=150, null=True)),
                ('location_id', models.CharField(blank=True, max_length=150, null=True)),
                ('source_identifier', models.CharField(blank=True, max_length=150, null=True)),
                ('source_url', models.URLField(blank=True, null=True)),
                ('processed_at', models.DateTimeField()),
                ('device_id', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_locale', models.CharField(blank=True, max_length=4, null=True)),
                ('app_id', models.CharField(blank=True, max_length=50, null=True)),
                ('browser_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('landing_site_ref', models.CharField(blank=True, max_length=50, null=True)),
                ('order_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]