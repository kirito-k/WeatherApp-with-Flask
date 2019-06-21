import requests
from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = '31117d4fd61be88575a2fa5b5bb1a308'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as e:
        print(e)
        data = None

    return data