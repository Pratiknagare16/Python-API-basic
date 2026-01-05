import requests

def get_weather(city_name):
    print("\nSearching weather for:", city_name)

    
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    if "results" not in geo_data:
        print(" City not found.")
        return

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

 
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    current = weather_data["current_weather"]

    print("\n Weather in", city_name.title())
    print(" Temperature:", current["temperature"], "°C")
    print(" Wind Speed:", current["windspeed"], "km/h")



city = input("Enter a city: ")
get_weather(city)
