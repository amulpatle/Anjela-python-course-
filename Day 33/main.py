import requests
from datetime import datetime
MY_LAT = 21.812876
MY_LOG = -80.183830
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    print(response.status_code)

    data = response.json()
    iss_latitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]
    iss_position = (iss_latitude,iss_longitude)
    # print(data)
    print(iss_position)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT and MY_LOG -5 <= iss_longitude <= MY_LOG+5:
        return True
def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LOG,
        "formatted":0
    }


    resonponse = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    resonponse.raise_for_status()
    data = resonponse.json()

    # print(data["results"]["sunrise"])
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now().hour
    
    if time_now >=sunset or time_now <=sunrise:
        return True
# print(time_now.hour)


if is_iss_overhead() && is_night():
    # THen send sms