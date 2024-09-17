import mysql.connector
import pandas as pd

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",  # Your MySQL server host
    user="root",       # Your MySQL username
    password="Harshil#1711",  # Your MySQL password
    database="zomato_db"  # Name of the database
)

cursor = conn.cursor()

# Create a table for restaurants (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id INT PRIMARY KEY,
    name TEXT,
    country_code INT,
    city TEXT,
    address TEXT,
    locality TEXT,
    latitude FLOAT,
    longitude FLOAT,
    cuisines TEXT,
    average_cost_for_two INT,
    currency TEXT,  -- Using TEXT for variable-length data
    has_table_booking VARCHAR(5),
    has_online_delivery VARCHAR(5),
    is_delivering_now VARCHAR(5),
    price_range INT,
    aggregate_rating FLOAT,
    rating_color VARCHAR(10),
    rating_text TEXT,
    votes INT
)
''')

# Load the CSV data into a pandas dataframe
# Load the CSV data into a pandas dataframe with specified encoding
df = pd.read_csv('zomato.csv', encoding='ISO-8859-1')

# Insert the data into the MySQL table
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO restaurants (
            restaurant_id, name, country_code, city, address, locality, latitude, longitude,
            cuisines, average_cost_for_two, currency, has_table_booking, has_online_delivery, 
            is_delivering_now, price_range, aggregate_rating, rating_color, rating_text, votes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        row['Restaurant ID'], row['Restaurant Name'], row['Country Code'], row['City'], 
        row['Address'], row['Locality'], row['Latitude'], row['Longitude'], row['Cuisines'], 
        row['Average Cost for two'], row['Currency'], row['Has Table booking'], 
        row['Has Online delivery'], row['Is delivering now'], row['Price range'], 
        row['Aggregate rating'], row['Rating color'], row['Rating text'], row['Votes']
    ))


# Commit and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data loaded into MySQL database successfully!")
