import requests

api_key = "dasf63la81511809e1çf965" #dummy API Key

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
  data = response.json()                      
  temp = data['main']['temp']
  desc = data['weather'][0]['description']
  celsius = temp - 273
  print(f'Temperature: {temp} K or {int(celsius)} C°')
  print(f'Description: {desc}')
else:
  print('Error fetching weather data')
