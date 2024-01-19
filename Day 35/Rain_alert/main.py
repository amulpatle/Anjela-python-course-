import requests

api_key = "d3dadd08143f0f4659d57312ccb45296"
OWM_Endpooint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat":23.259933,
    "lon":-77.412613,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(OWM_Endpooint,params=parameters)

weather_data = response.json()

print(weather_data["list"][1]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")