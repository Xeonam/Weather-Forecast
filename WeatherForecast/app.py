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
    european_cities = ["Paris", "London", "Berlin", "Madrid", "Rome", "Athens", "Budapest", "Debrecen"]

    weather_list = []

    for city in european_cities:
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

        
    return render_template('europe.html', weather=weather_list)

@app.route("/america")
def get_american_weather():
    american_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Francisco"]


    weather_list = []

    for city in american_cities:
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

        
    return render_template('europe.html', weather=weather_list)

if __name__ == '__main__':
    app.run(debug=True)
