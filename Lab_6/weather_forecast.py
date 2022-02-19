from datetime import datetime
from distutils.log import error
import requests
import os

key = os.environ.get('WEATHER_KEY')
print(key)

url = 'https://api.openweathermap.org/data/2.5/forecast'
query = { 'q': 'minneapolis,us' , 'units':'imperial', 'appid': key}
data = requests.get(url, params=query).json()

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Sorry, could not get weather')
    else:
        get_temp(weather_data)

def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-leter country code: ').strip()

    location = f'{city}, {country}'
    return location

def get_current_weather(location , key):
    try:
        query = { 'q': location, 'units':'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex

def get_temp(weather_data):
    try:
        list_of_forecast = weather_data['list']
        print('%-20s %-14s %-18s %-10s' % ('Date', 'Temperature F', 'Description', 'Wind speed'))
        print('-'*65)
        for forecast in list_of_forecast:
            temp = forecast['main']['temp']
            timestamp = forecast['dt']
            desc = forecast['weather'][0]['description']
            wind = forecast['wind']['speed']
    
            forecast_date = datetime.fromtimestamp(timestamp)
            print('%-20s %-14s %-18s %-10s' % (forecast_date, temp, desc, wind))
    except KeyError:
        print('This data is not in the formart expected')
        return 'Unknown'

if __name__ == '__main__':
    main()