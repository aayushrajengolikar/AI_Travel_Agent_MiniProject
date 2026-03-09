import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

def get_coordinates(city):

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

    response = requests.get(url).json()

    lat = response["results"][0]["latitude"]
    lon = response["results"][0]["longitude"]

    return lat, lon


def get_weather(city):

    lat, lon = get_coordinates(city)

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto"

    data = requests.get(weather_url, verify=False).json()

    return data