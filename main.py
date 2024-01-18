# app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace these with your own API keys
OWM_API_KEY = '677a830caa3df141310ac5e95acd6dd0'
TRIPADVISOR_API_KEY = '05dc11d90ef6ac68ee73f326b35463f1'
UNSPLASH_ACCESS_KEY = 'd903707ed3dd588bd03f7a71b269aa20'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    weather_data = get_weather_data(city)
    return render_template('weather.html', city=city, weather_data=weather_data)

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    city = request.form['city']
    recommendations = get_travel_recommendations(city)
    return render_template('recommendations.html', city=city, recommendations=recommendations)

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}'
    response = requests.get(url)
    data = response.json()

    weather = {
        'description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
    }

    return weather

def get_travel_recommendations(city):
    url = f'https://api.tripadvisor.com/data/1.0/location/{city}/reviews?key={TRIPADVISOR_API_KEY}'
    response = requests.get(url)
    data = response.json()

    recommendations = [review['text'] for review in data['reviews']]

    return recommendations

if __name__ == '__main__':
    app.run(debug=True)
