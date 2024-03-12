import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('API_KEYS')

def get_lan_lon(city_name, state_code,country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()

    print(resp)

get_lan_lon('Toronto', 'ON', 'Canada', api_key)
