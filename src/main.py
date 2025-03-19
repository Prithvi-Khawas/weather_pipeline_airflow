from extract import extract_api_data
from transform import transform_weather_data
from load import load_data_to_db


final_data = extract_api_data(city='Nepal',country='NP')

if final_data:
    # Transform the data
    transformed_df = transform_weather_data(final_data)
    print("Transformed Data:")
    print(transformed_df)
    
    # Load the transformed data into the database
    load_data_to_db(transformed_df)
else:
    print("ETL process failed: Data extraction or transformation issue.")
    

