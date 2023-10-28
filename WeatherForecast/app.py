import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Az OpenWeatherMap API kulcs
API_KEY = "32c72d349a6a2395fa06b5cf197b10f2"

# Az API végpontja
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Alapértelmezett város, ha nincs megadva
DEFAULT_CITY = "Budapest"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', DEFAULT_CITY)

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Celsius-ban
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return jsonify(data)
    else:
        return jsonify({'error': 'Nem sikerült lekérni az időjárási adatokat'}), 500

if __name__ == '__main__':
    app.run(debug=True)
