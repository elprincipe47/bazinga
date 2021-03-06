from django.db import models
import uuid

# Create your models here.


class Order(models.Model):

    id = models.CharField(primary_key=True, max_length=30, editable=False)
    email = models.EmailField(null=False, blank=False)
    closed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    gateway = models.CharField(max_length=60, blank=True, null=True)
    test = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    subtotal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_weight = models.IntegerField(blank=True, null=True)
    total_tax = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    taxes_included = models.BooleanField(default=False)
    currency = models.CharField(max_length=4, blank=True, null=True)
    financial_status = models.CharField(max_length=20, blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    total_discounts = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_line_items_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cart_token = models.CharField(max_length=50, blank=True, null=True)
    buyer_accepts_marketing = models.BooleanField(default=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    referring_site = models.URLField(blank=True, null=True)
    landing_site = models.URLField(blank=True, null=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    cancel_reason =models.CharField(max_length=20, blank=True, null=True)
    total_price_usd = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    checkout_token = models.CharField(max_length=50, blank=True, null=True)
    reference = models.CharField(max_length=150, blank=True, null=True)
    user_id = models.CharField(max_length=150, blank=True, null=True)
    location_id = models.CharField(max_length=150, blank=True, null=True)
    source_identifier = models.CharField(max_length=150, blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    device_id = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    customer_locale = models.CharField(max_length=4, blank=True, null=True)
    app_id = models.CharField(max_length=50, blank=True, null=True)
    browser_ip = models.CharField(max_length=50, blank=True, null=True)
    landing_site_ref = models.CharField(max_length=50, blank=True, null=True)
    order_number = models.CharField(max_length=50, blank=True, null=True)
    fulfillment_status = models.CharField(max_length=50, blank=True, null=True)
    source_name = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    order_status_url = models.CharField(max_length=255, blank=True, null=True)
    presentment_currency = models.CharField(max_length=4, blank=True, null=True)
    checkout_id = models.CharField(max_length=20, blank=True, null=True)
