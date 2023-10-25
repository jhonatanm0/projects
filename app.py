import json
import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
from flask import Flask, render_template, request, jsonify

# ...

app = Flask(__name__ ,static_folder='static')

# ...

def get_data():
    # Read data from the sensor_data.json file
    try:
        with open("sensor_data.json", "r") as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f'Error: {e}')
        return None

# ...

@app.route('/')
def index():
    # Retrieve data from the JSON file
    data = get_data()
    return render_template('Greenhouse.html', data=data)  # Pass data to the template

@app.route('/get_json.data', methods=['GET'])
def get_json_data():
    # Retrieve data from the JSON file and serve it as JSON
    data = get_data()
    return jsonify(data)

# ...

if __name__ == '__main__':
    app.run(debug=True)