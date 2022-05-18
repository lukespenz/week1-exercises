import requests


def get_weather():
    api = 'd9d746f3397924f827bc9690db10afc7'
    lat = '40.758701'
    long = '-111.876183'

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api}&units=imperial"

    requestAPI = requests.get(url)
    json = requestAPI.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp-min': temp_min,
            'temp-max': temp_max}


# Print Results
weather_dict = get_weather()
print("Today's forecast is", weather_dict.get('description'))
print("The maximum temperature is", weather_dict.get('temp-max'))
print("The minimum temperature is", weather_dict.get('temp-min'))
