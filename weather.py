import requests
from twilio.rest import Client
import os

ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
KEY =  os.getenv('WEATHER_API_KEY')
LAT = os.getenv('LAT')
LONG = os.getenv('LONG')

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_from = os.getenv('TWILIO_FROM')
twilio_to = os.getenv('TWILIO_TO')

params = {
    'lat': LAT,
    'lon': LONG,
    'appid': KEY,
    'cnt': 4
}

response = requests.get(url=ENDPOINT, params=params)
response.raise_for_status()
data = response.json()
#print(data['list'][0]['weather'][0]['id'])

will_rain = False

for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It is going to rain today. Remember to bring an ☂',
        from_=twilio_from,
        to=twilio_to
    )

    print(message.status)