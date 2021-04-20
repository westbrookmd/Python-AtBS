#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

# hiding my api key
key_file = open('key_file.txt')
key_content = key_file.read()

APPID = key_content

import json, requests, sys

# Get zip code
zip = input("Enter ZIP: ")

# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/weather?zip=%s,us&units=imperial&appid=%s' % (zip,APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['main']
print('Current weather in %s:' % (zip))
print('The temperature right now is ' + str(w['temp']) + ' Fahrenheit.')
print('It feels like ' + str(w['feels_like']) + ' Fahrenheit.')


# Extra stuff for a different format
"""print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])"""
