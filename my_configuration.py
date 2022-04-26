import configparser
config = configparser.RawConfigParser()
config.read(filenames="config.properties")
openweather_api_key = config.get("openweathermap.org", "openweather.api.key")

openweather_api_url = "https://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"
openweather_api_url2 = "https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_name}&appid={api_key}"
openweather_api_url3 = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"

twilio_sid = config.get("twilio.com", "twilio.api.sid")
twilio_token = config.get("twilio.com", "twilio.api.token")

my_phone_number = config.get("my-info", "phone.number.me")