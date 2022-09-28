import requests
from datetime import datetime

# response = requests.get("http://api.open-notify.org/iss-now.json")
#
# # To get the status code of response
# print(response.status_code)
#
# # To get the status message
# print(response.raise_for_status())
#
# # To get the data returned by the request
# print(response.json())


MY_LAT = 21.486935
MY_LNG = 86.924599


parameters={
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(":")[0]
sunset = data["results"]["sunset"].split('T')[1].split(":")[0]

print(sunset)

timenow = datetime.now().hour
print(timenow)