import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import os

API_KEY = "d8b8abbcd7dd4061753c9d9b234829b6"
F1_SCHEDULE_URL = "https://www.formula1.com/en/latest/article/fia-and-formula-1-announces-calendar-for-2025.48ii9hOMGxuOJnjLgpA5qS.html"

def get_f1_race_schedule():
    response = requests.get(F1_SCHEDULE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    races = []
    race_blocks = soup.find_all('div', class_='f1-race-block')  
    for race in race_blocks:
        location = race.find('span', class_='location').text.strip()
        date = race.find('span', class_='date').text.strip()

        race_date = datetime.datetime.strptime(date, '%d %b %Y').strftime('%Y-%m-%d')
        races.append({'location': location, 'date': race_date})

    return races

def get_lat_lon(location):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={API_KEY}"
    response = requests.get(geo_url).json()
    if response:
        return response[0]['lat'], response[0]['lon']
    return None, None

def get_weather_data(lat, lon, date):
    timestamp = int(datetime.datetime.strptime(date, '%Y-%m-%d').timestamp())
    weather_url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={API_KEY}"
    response = requests.get(weather_url).json()
    return response

def main():
    race_schedule = get_f1_race_schedule()
    print(race_schedule)

    weather_data = []

    for race in race_schedule:
        location = race['location']
        race_date = race['date']

        print(f"Fetching weather for {location} on {race_date}...")

        lat, lon = get_lat_lon(location)
        if lat and lon:
            weather = get_weather_data(lat, lon, race_date)
            weather_data.append({
                'location': location,
                'date': race_date,
                'temperature': weather['current']['temp'],
                'humidity': weather['current']['humidity'],
                'weather_description': weather['current']['weather'][0]['description']
            })
        else:
            print(f"Could not get coordinates for {location}")

    df = pd.DataFrame(weather_data)
    df.to_csv('example_output.csv', index=False)
    print("Data saved to example_output.csv")

if __name__ == "__main__":
    main()
