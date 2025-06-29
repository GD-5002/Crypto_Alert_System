# alerts.py

def check_price_alerts(prices, alert_ranges):
    alerts_triggered = []

    for coin, price_data in prices.items():
        current_price = price_data.get('usd')
        if current_price is None:
            continue

        min_price = alert_ranges[coin]['min']
        max_price = alert_ranges[coin]['max']

        if min_price <= current_price <= max_price:
            alerts_triggered.append((coin, current_price))

    return alerts_triggered
