import os
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Az OpenWeatherMap API kulcs
API_KEY = "32c72d349a6a2395fa06b5cf197b10f2"

# Az API végpontja
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Alapértelmezett város, ha nincs megadva
DEFAULT_CITY = "Budapest"

def get_weather_data(cities):
    weather_list = []

    for city in cities:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'temp_max': data['main']['temp_max'],
                'temp_min': data['main']['temp_min'],
                'description': data['weather'][0]['description']
            }

            weather_list.append(weather)

    return weather_list

@app.route('/', methods=['GET'])
def main():
    return render_template('main_menu.html')

@app.route('/city_input', methods=['GET'])
def city_input():
    return render_template('city_input.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', DEFAULT_CITY)

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric' 
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'lat': data['coord']['lat'],
            'lon': data['coord']['lon'],
            'temperature': data['main']['temp'],
            'temp_max': data['main']['temp_max'],
            'temp_min': data['main']['temp_min'],
            'humidity': data['main']['humidity'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'deg': data['wind']['deg'],
            'speed': data['wind']['speed']
        }
        return render_template('weather.html', weather=weather)
    else:
        return jsonify({'error': 'Nem sikerült lekérni az időjárási adatokat'}), 500
    

@app.route("/europe")
def get_european_weather():
    name = "European"
    wikipedia = "Europe"
    european_cities = ["Paris", "London", "Berlin", "Madrid", "Rome", "Athens", "Budapest", "Debrecen"]
    weather_list = get_weather_data(european_cities)
    return render_template('weather_forecast.html', name=name, weather=weather_list, wikipedia=wikipedia)

@app.route("/america")
def get_american_weather():
    name = "American"
    wikipedia = "North_America"
    american_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Ottawa", "San Antonio", "San Francisco"]
    weather_list = get_weather_data(american_cities)
    return render_template('weather_forecast.html', name=name, weather=weather_list, wikipedia=wikipedia)

@app.route("/asia")
def get_asian_weather():
    name = "Asian"
    wikipedia = "Asia"
    asian_cities = ["Bangkok", "Tokyo", "Jakarta", "Hanoi", "Peking", "Hongkong", "Manila", "Shanghai"]
    weather_list = get_weather_data(asian_cities)
    return render_template('weather_forecast.html', name=name, weather=weather_list, wikipedia=wikipedia)


if __name__ == '__main__':
    app.run(debug=True)
