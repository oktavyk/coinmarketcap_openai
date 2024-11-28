# -*- coding: utf-8 -*-

import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {
    "X-CMC_PRO_API_KEY": "125ec6dc-759b-463a-ba53-16801acb9f6a",
    "Content-Type": "application/json"
}
params = {
    "start": 1,
    "limit": 10,
    "convert": "USD"
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Проверяет наличие ошибок HTTP
    print(response.json())  # Печатает JSON-ответ
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except Exception as e:
    print(f"Другая ошибка: {e}")
