import requests
import sys

def get_weather(city):
    try:
        
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        print("Raw Geocoding Response:")
        print(geo_data)

        if "results" not in geo_data:
            print("City not found.")
            return

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]

       
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        print("\nRaw Weather Response:")
        print(weather_data)

        current = weather_data["current_weather"]

        temp_c = current["temperature"]
        temp_f = (temp_c * 9/5) + 32
        wind = current["windspeed"]

        print("\nCity:", city_name)
        print("Temperature:", temp_c, "°C /", round(temp_f, 2), "°F")
        print("Wind Speed:", wind, "km/h")

    except requests.exceptions.RequestException:
        print("Network error.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather_cli.py <city>")
    else:
        get_weather(sys.argv[1])