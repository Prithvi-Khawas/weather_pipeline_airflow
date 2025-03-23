import requests


def extract_api_data(countries_and_cities):
    API_KEY = '26c2425b238c58c09462c029b85e0cd4'
    results = []
    
    for country, city in countries_and_cities:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}"
        response = requests.get(weather_url)
    
        if response.status_code == 200:
            print("data fetched successfully")
            json_data = response.json()
            results.append(json_data)
        else:
            print("Unable to fetch")
    
    return results
