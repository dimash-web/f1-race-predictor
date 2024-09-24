# F1 Race Weather Data Pipeline

## Project Overview
This project scrapes the 2025 F1 race schedule from the official Formula 1 website and uses the OpenWeatherMap API to pull weather data for each race location and date. The output is a CSV file containing the race location, date, and weather data.

## Features

- **F1 Schedule Location Scraper**: Scrapes a list of the places where F1 races will be held next season.
- **Uses the OpenWeather API**: Once the scraping is completed, locations are matched with their coordinates and weather data for the dates of the races is pulled.
- **Web Scraping Tools**: Utilizes **BeautifulSoup** to extract relevant data.

## Usage
1. Clone the repository.
2. Install dependencies:
   pip install -r requirements.txt
3. Set up your OpenWeatherMap API key in main.py
4. Run it!
