from flask import Flask, jsonify, request, render_template
import mysql.connector
from math import radians, sin, cos, sqrt, atan2
from cache import SimpleCache  # Import the SimpleCache class

app = Flask(__name__, template_folder='templates')

# Initialize the SimpleCache
cache = SimpleCache()

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshil#1711",
        database="zomato_db"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restaurant/<int:id>', methods=['GET'])
def get_restaurant(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM restaurants WHERE `Restaurant ID` = %s", (id,))
    restaurant = cursor.fetchone()
    conn.close()
    if restaurant:
        return jsonify(restaurant)
    return jsonify({"error": "Restaurant not found"}), 404

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    offset = (page - 1) * per_page

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM restaurants LIMIT %s OFFSET %s", (per_page, offset))
    restaurants = cursor.fetchall()
    conn.close()
    return jsonify(restaurants)

@app.route('/search_by_text', methods=['GET'])
def search_by_text():
    search_term = request.args.get('q', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    offset = (page - 1) * per_page
    
    # Generate a unique cache key based on query parameters
    cache_key = f"search_{search_term}_{page}_{per_page}"
    
    # Check if result is in cache
    cached_result = cache.get(cache_key)
    if cached_result:
        return jsonify(cached_result)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT * FROM restaurants 
    WHERE `Restaurant Name` LIKE %s OR `Description` LIKE %s
    LIMIT %s OFFSET %s
    """
    search_param = f"%{search_term}%"
    cursor.execute(query, (search_param, search_param, per_page, offset))
    
    restaurants = cursor.fetchall()
    
    # Get total count for pagination
    cursor.execute(""" 
    SELECT COUNT(*) as count FROM restaurants 
    WHERE `Restaurant Name` LIKE %s OR `Description` LIKE %s
    """, (search_param, search_param))
    total_count = cursor.fetchone()['count']

    conn.close()
    
    result = {
        "restaurants": restaurants,
        "total_count": total_count,
        "page": page,
        "per_page": per_page
    }
    
    # Cache the result
    cache.set(cache_key, result, timeout=300)  # Cache for 5 minutes

    return jsonify(result)

@app.route('/search', methods=['GET'])
def search_restaurants():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    radius = float(request.args.get('radius', 3))  # Default radius: 3 km

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Haversine formula to calculate distance
    cursor.execute("""
    SELECT *, 
        6371 * 2 * ASIN(SQRT(
            POWER(SIN((RADIANS(%s) - RADIANS(Latitude)) / 2), 2) +
            COS(RADIANS(%s)) * COS(RADIANS(Latitude)) *
            POWER(SIN((RADIANS(%s) - RADIANS(Longitude)) / 2), 2)
        )) AS distance
    FROM restaurants
    HAVING distance <= %s
    ORDER BY distance
    """, (lat, lat, lon, radius))

    restaurants = cursor.fetchall()
    conn.close()
    return jsonify(restaurants)

if __name__ == '__main__':
    app.run(debug=True)
