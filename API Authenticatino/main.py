import requests

api_key = "9b7a98a6886a67b8f30976ed6ac05f08"
OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": 20.068319,
    "lon": 84.730126,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(OWM_endpoint, params=weather_params)
# print(response.status_code)
weather_data = response.json()
last_12_hours = weather_data["hourly"][:12]
will_rain = False
for hour_data in last_12_hours:
    condition_code = hour_data["weather"][0]['id']
    if condition_code < 700: # if less than 700 then it will rain
        will_rain = True

if will_rain:
    print("Bring Umbrella")

