#! python3
# prints the weather from a location input from terminal

import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# load JSON data into a variable
weatherData = json.loads(response.text)

# print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])

# this doesn't work, something is wrong with my API call
# I signed up with the service but I suspect I'm not using my key correctly
# but their documentation is difficult, so I'm letting this one sit