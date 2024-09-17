import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Read the CSV file
df = pd.read_csv('zomato.csv', encoding='ISO-8859-1')

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harshil#1711"
)

cursor = db.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS zomato_db")
cursor.execute("USE zomato_db")

# Create table with the correct column names and TEXT for longer fields
create_table_sql = """
CREATE TABLE IF NOT EXISTS restaurants (
    `Restaurant ID` INT PRIMARY KEY,
    `Restaurant Name` TEXT,
    `Country Code` INT,
    `City` TEXT,
    `Address` TEXT,
    `Locality` TEXT,
    `Locality Verbose` TEXT,
    `Longitude` FLOAT,
    `Latitude` FLOAT,
    `Cuisines` TEXT,
    `Average Cost for two` INT,
    `Currency` VARCHAR(20),
    `Has Table booking` VARCHAR(10),
    `Has Online delivery` VARCHAR(10),
    `Is delivering now` VARCHAR(10),
    `Switch to order menu` VARCHAR(10),
    `Price range` INT,
    `Aggregate rating` FLOAT,
    `Rating color` VARCHAR(20),
    `Rating text` VARCHAR(20),
    `Votes` INT
)
"""
cursor.execute(create_table_sql)

db.commit()
db.close()

# Use SQLAlchemy to bulk insert data
engine = create_engine(f"mysql+mysqlconnector://root:Harshil#1711@localhost/zomato_db")

# Convert boolean-like columns to string
bool_columns = ['Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu']
for col in bool_columns:
    df[col] = df[col].map({0: 'False', 1: 'True'})

# Insert data into the database
df.to_sql('restaurants', con=engine, if_exists='replace', index=False, chunksize=1000)

print("Database setup complete and data imported successfully.")