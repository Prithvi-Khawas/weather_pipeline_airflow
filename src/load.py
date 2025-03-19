from sqlalchemy import create_engine

def load_data_to_db(loading_data):
    # Define the database connection URL
    database_url = "postgresql://postgres:prithvi@localhost:5432/weather_pipeline"
    
    # Create the SQLAlchemy engine
    engine = create_engine(database_url)
    
    # Load the DataFrame into the database table
    loading_data.to_sql('weather_data', engine, if_exists='append', index=False)
    
    print("Data loaded successfully in database")
