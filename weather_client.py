import requests   #importing the request module
from datetime import datetime

def get_weather(city_name, api_key):    #defining the get weather function
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

    response = requests.get(base_url, params = params)

    if response.status_code  == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        city = data['name']
        country = data['sys']['country']
        humidity = data['main']['humidity']         
        wind_speed = data['wind']['speed']  

        print(f"\n weather in {city}, {country}")
        print(f"\n Temperature: {temperature}°C")
        print(f"\n Condition: {weather.capitalize()}")
        print(f"\n Humidity: {humidity}")
        print(f"\n Windspeed: {wind_speed}")
        
    else:
        print(f"\n city not found or API error occur")

#Get 5days forecast
def get_forecast(city_name, api_key):
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

    response = requests.get(forecast_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\n5-Day Forecast for {city_name.capitalize()}:\n")

        forecasts = data['list']
        printed_dates = set()

        for forecast in forecasts:
            dt_txt = forecast['dt_txt']
            date = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
            day = date.strftime('%A, %d %B')

            if date.hour == 12 and day not in printed_dates:
                temp = forecast['main']['temp']
                description = forecast['weather'][0]['description'].capitalize()
                print(f"{day}: {temp}°C, {description}")
                printed_dates.add(day)
    else:
        print("\nUnable to fetch forecast.")

# Main function
def main():
    print("Weather Checker")

    # Let user input multiple cities
    cities_input = input("Enter city names separated by commas (e.g., Lagos, Abuja, London): ").strip()

    # Split and clean up the city names
    cities = [city.strip() for city in cities_input.split(',') if city.strip()]

    api_key = "df792f7bedf186ccf3d9d0b3f00d1ecc"

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("Please set your OpenWeatherMap API key in the script.")
        return

    for city in cities:
        print("\n" + "=" * 40)
        get_weather(city, api_key)
        get_forecast(city, api_key)
        print("=" * 40)
    
if __name__ == "__main__":
    main()
