from flask import Flask, request, jsonify
import threading
import pandas as pd
import os

# Import your existing scraping functions
from tryex import executefuntion, save_to_csv

app = Flask(__name__)

# Example route to test the API
@app.route('/')
def hello_world():
    return "Flight Scraper API is running!"

# Route to execute the scraping function
@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    
    # Extract parameters from the request
    file_path = data.get('file_path')
    trip_type = data.get('trip_type')
    going_date = data.get('going_date')
    returning_date = data.get('returning_date')
    adult = data.get('adult')
    children = data.get('children')
    infants = data.get('infants')
    proxy_list = data.get('proxy_list')
    integer_input = data.get('integer_input')
    
    if not file_path or not trip_type or not going_date or not adult or not proxy_list or not integer_input:
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        thread = threading.Thread(target=executefuntion, args=(file_path, trip_type, going_date, returning_date, adult, children, infants, proxy_list, integer_input))
        thread.start()
        
        return jsonify({"message": "Scraping started successfully!"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
