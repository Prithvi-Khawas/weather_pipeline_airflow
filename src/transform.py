import pandas as pd

def transform_weather_data(data):
    if data:
        weather_data = {
            "longitude": data['coord']['lon'],
            "latitude": data['coord']['lat'],
            "id": data['weather'][0]['id'],  # Access the first item in the 'weather' list
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "humidity": data['main']['humidity'],
            "country_name": data['sys']['country'],
            "city_name": data['name']  # Corrected to fetch city name
        }
        
        # Convert to DataFrame
        df = pd.DataFrame([weather_data])  # Wrap dictionary in a list
        return df
    else:
        print("Error: No data to transform.")
        return None


