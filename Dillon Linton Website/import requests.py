import requests
from datetime import datetime, timedelta

def get_weather(city: str, api_key: str):
    # Request weather forecast
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")
    data = response.json()

    # Get weather for today and tomorrow
    now = datetime.now()
    today = [item for item in data['list'] if datetime.fromtimestamp(item['dt']).date() == now.date()]
    tomorrow = [item for item in data['list'] if datetime.fromtimestamp(item['dt']).date() == (now + timedelta(days=1)).date()]

    # Check if it's going to rain
    rain_today = any('rain' in item['weather'][0]['description'].lower() for item in today)
    rain_tomorrow = any('rain' in item['weather'][0]['description'].lower() for item in tomorrow)

    return rain_today, rain_tomorrow

def main():
    api_key = 'your_api_key'
    city = input("What's your location? ")
    washing_car = input("Will you be washing your car today? (yes/no) ")

    rain_today, rain_tomorrow = get_weather(city, api_key)

    if washing_car.lower() == 'yes':
        if rain_today or rain_tomorrow:
            print("It's not a good day to wash your car.")
        else:
            print("It's a good day to wash your car.")
    else:
        print("Okay, have a nice day!")

if __name__ == "__main__":
    main()
