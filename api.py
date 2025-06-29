import requests
import json
import os

BASE_URL = "https://api.coingecko.com/api/v3"

def get_simple_price(ids, currency='usd'):
    url = f"{BASE_URL}/simple/price"
    params = {'ids': ','.join(ids), 'vs_currencies': currency}
    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error in get_simple_price: {e}")
        return {}

import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def get_supported_coins():
    url = f"{BASE_URL}/coins/list"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error in get_supported_coins: {e}")
        return []  

def get_trending_coins():
    url = f"{BASE_URL}/search/trending"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f" Error in get_trending_coins: {e}")
        return {}
