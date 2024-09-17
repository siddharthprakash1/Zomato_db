![image](https://github.com/user-attachments/assets/edbaa17b-05a1-41b4-bc32-a535612d13a6)
![image](https://github.com/user-attachments/assets/4c36bacb-617a-42e4-940b-a697135b598a)
# Zomato Restaurant API

This project is a Flask-based API that provides information about restaurants, sourced from a Zomato dataset stored in a MySQL database. It offers various endpoints for retrieving restaurant data, searching by location, and text-based searching.

## Features

- Retrieve individual restaurant details
- List restaurants with pagination
- Search restaurants by geographical location (latitude, longitude, and radius)
- Text-based search for restaurants
- Simple caching mechanism for improved performance

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- MySQL server
- Zomato dataset imported into a MySQL database named `zomato_db`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/zomato-restaurant-api.git
   cd zomato-restaurant-api
   ```

2. Install the required packages:
   ```
   pip install flask mysql-connector-python
   ```

3. Set up your MySQL database:
   - Create a database named `zomato_db`
   - Import the Zomato dataset into this database

4. Update the database connection details in `app.py`:
   ```python
   host="localhost",
   user="root",
   password="your_password",
   database="zomato_db"
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. The server will start running on `http://localhost:5000`

3. You can now use the following endpoints:

   - GET `/`: Renders the main HTML page
   - GET `/restaurant/<id>`: Get details of a specific restaurant
   - GET `/restaurants`: List restaurants (with pagination)
   - GET `/search`: Search restaurants by location
   - GET `/search_by_text`: Text-based search for restaurants

## API Endpoints

### Get Restaurant Details

```
GET /restaurant/<id>
```

Returns details of a specific restaurant.

### List Restaurants

```
GET /restaurants?page=<page_number>&per_page=<items_per_page>
```

Returns a paginated list of restaurants.

### Search by Location

```
GET /search?lat=<latitude>&lon=<longitude>&radius=<radius_in_km>
```

Returns restaurants within the specified radius of the given coordinates.

### Text Search

```
GET /search_by_text?q=<search_term>&page=<page_number>&per_page=<items_per_page>
```

Performs a text-based search on restaurant names and descriptions.

## Frontend

The project includes a simple HTML frontend (`index.html`) that allows users to interact with the API through a web interface.

## Caching

The project implements a simple caching mechanism for the text search functionality to improve performance. Search results are cached for 5 minutes.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please contact [siddharth](iamsid0011@gmail.com).
