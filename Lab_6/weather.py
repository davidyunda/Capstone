from pprint import pprint
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q=minneapolis,us&units=imperial&appid=a4df1057eaab2c75de7de6fe62b89355'

data = requests.get(url).json()

pprint(data)

