import requests
import os

API_KEY = "58cef9659cdf58d5e41f169d59e058dd"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def extract_temperatures(data):
    temps = []
    for item in data['list']:
        temps.append(item['main']['temp'])
    return temps

if __name__ == "__main__":
    city = input("Enter city name: ")
    data = get_weather_data(city)
    if data:
        temperatures = extract_temperatures(data)
        print(f"Temperatures for the next 5 days: {temperatures}")