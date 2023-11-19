from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import psycopg2
DATABASE_URL = 'postgresql://postgres:12345678@localhost:5432/temp_db'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# import data in postgresql using csv file
def import_data():

    # Replace 'your_file.csv' with the path to your CSV file
    csv_file_path = 'aws_billing_data.csv'
    table_name = 'aws_billing'

    # Read CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Create table in PostgreSQL
    df.to_sql(table_name, engine, index=False, if_exists='replace')

    # Close the database connection
    engine.dispose()

    print(f'Table {table_name} created and data imported successfully.')

# call this function while you want to import the csv file otherwise comment out the function
# import_data()