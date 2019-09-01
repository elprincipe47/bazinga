
def clean_payload(payload):
    unuesed_fields = ["discount_applications", "discount_codes","tax_lines", "note_attributes", "payment_gateway_names","processing_method","total_line_items_price_set","total_line_items_price_set", "total_discounts_set","total_shipping_price_set","subtotal_price_set","total_price_set","total_tax_set","total_tip_received","admin_graphql_api_id","line_items","shipping_lines","billing_address","shipping_address","fulfillments","refunds","customer","client_details","payment_details"]
    for key in unuesed_fields:
        if key in payload:
            del payload[key]
    return payload
