import my_configuration
import requests

api_key = my_configuration.openweather_api_key

# get your latitude and longitude from https://www.latlong.net/
lat = 3.139003
lon = 101.686852

parameters = {
    #Required Parameters
    "appid" : my_configuration.openweather_api_key,
    "lat" : lat,
    "lon" : lon,

    #Optional Parameter
    "exclude" : "current,daily,minutely"
}
weather_response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()
weather_hourly_data = weather_data["hourly"]

print("Next 12 hour weather data")
for weather in weather_hourly_data[:12]:
    hourly_data = weather["weather"]
    print(hourly_data)


