from extract import extract_api_data
from transform import transform_weather_data
from load import load_data_to_db
import pandas as pd

# Define your countries and cities
countries_and_cities = [
    ("NP", "Kathmandu"),
    ("US", "New York"),
    ("JP", "Tokyo"),
    ("FR", "Paris"),
    ("AE", "Dubai"),
]

# Run the ETL process
final_data = extract_api_data(countries_and_cities)

if final_data:
    # Initialize an empty DataFrame to store all transformed data
    all_transformed_data = pd.DataFrame()

    # Transform data for each city
    for city_data in final_data:
        transformed_df = transform_weather_data(city_data)
        if transformed_df is not None:
            all_transformed_data = pd.concat([all_transformed_data, transformed_df], ignore_index=True)

    print("Transformed Data:")
    print(all_transformed_data)

    # Load the combined transformed data into the database
    if not all_transformed_data.empty:
        load_data_to_db(all_transformed_data)
    else:
        print("No data available to load into the database.")
else:
    print("ETL process failed: Data extraction or transformation issue.")
