import psycopg2

def load_data_to_db(transformed_df):
    # Establish connection to PostgreSQL
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="prithvi",
        port=5432,
        dbname="weather_pipeline"
    )
    try:
        cursor = connection.cursor()

        # Loop through each row in the DataFrame and insert it into the table
        for index, row in transformed_df.iterrows():
            cursor.execute(
                """
                INSERT INTO weather_data (longitude, latitude, id, humidity, country_name, city_name, temperature, feels_like)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (row['longitude'], row['latitude'], row['id'], row['humidity'], row['country_name'], row['city_name'], row['temperature'], row['feels_like'])
            )

        # Commit changes to the database
        connection.commit()
        print("Data loaded successfully into the database.")

    except Exception as e:
        # Handle exceptions and roll back changes if something goes wrong
        print(f"An error occurred: {e}")
        connection.rollback()

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

