#!/bin/python
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="weather_app")
# Put in street address, city, and state or put in city and state

# Enter city name ',' state abbreviation
# ex. Omaha, NE or Miami, FL
city = input('City:')
location = geolocator.geocode(f'{city}')
print(location.raw)
lat = (location.latitude) 
lon = (location.longitude)
print('-----------------------------')

weather = pd.read_html(f'https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}')
weather_stats = pd.read_html(f'https://forecast.weather.gov/MapClick.php?w0=t&w2=hi&w3=sfcwind&w3u=1&w5=pop&w6=rh&w10u=0&w13u=1&w14u=1&AheadHour=0&Submit=Submit&FcstType=digital&textField1={lat}&textField2={lon}&site=all&unit=0&dd=&bw=')

print('-----------------------------')
print('Total # of tables:', len(weather))

# prints all the tables
print(weather)
print('-----------------------------')
print('Total # of tables:', len(weather_stats))
print(weather_stats[7])
print('-----------------------------')
print(weather_stats[3])
