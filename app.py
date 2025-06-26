import pymysql
from flask import Flask, request, jsonify
from db_config import get_db_connection, close_db_connection
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.teardown_appcontext(close_db_connection)

@app.route('/')
def index():
    return 'Real Estate API is running!'

@app.route('/properties', methods=['POST'])
def add_property():
    data = request.json
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = """
        INSERT INTO properties (location, size, total_sqft, bath, price_lakhs, price_per_sqft)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            data['location'], data['size'], data['total_sqft'],
            data['bath'], data['price_lakhs'], data['price_per_sqft']
        ))
        conn.commit()
        return jsonify({"message": "Property inserted", "property_id": cursor.lastrowid})

@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    data = request.json
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = """
        UPDATE properties SET location=%s, size=%s, total_sqft=%s,
        bath=%s, price_lakhs=%s, price_per_sqft=%s WHERE property_id=%s
        """
        cursor.execute(sql, (
            data['location'], data['size'], data['total_sqft'],
            data['bath'], data['price_lakhs'], data['price_per_sqft'], property_id
        ))
        conn.commit()
        return jsonify({"message": "Property updated"})

@app.route('/filter', methods=['GET'])
def filter_properties():
    filters = []
    values = []

    for key in ['location', 'size', 'total_sqft', 'bath', 'price_lakhs', 'price_per_sqft']:
        if key in request.args:
            filters.append(f"{key} = %s")
            values.append(request.args.get(key))

    where_clause = " AND ".join(filters)
    sql = "SELECT * FROM properties"
    if where_clause:
        sql += f" WHERE {where_clause}"

    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor: 
            cursor.execute(sql, values)
            result = cursor.fetchall()
            return jsonify(result)
    finally:
        connection.close()

@app.route('/properties', methods=['GET'])
def list_properties():
    conn = get_db_connection()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM properties")
            return jsonify(cursor.fetchall())
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)