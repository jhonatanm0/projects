import json
import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

# Constants
DHTPIN = 12  # Digital pin
MAX_DATA_ENTRIES = 10

# Global variables
humidity = 0
temperature = 0
data_entries = []  # List to store the last 10 data entries

# Callback function to measure and update humidity and temperature
def Measure(data):
    global humidity, temperature
    if (data[1] == 0):  # Check if it's the DHT data
        humidity = data[4]
        temperature = data[5]

def setup():
    global board

    board = CustomTelemetrix()
    board.displayOn()
    board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)

def loop():
    global humidity, temperature, data_entries
    print("Humidity: {:.2f} %".format(humidity))
    print("Temperature: {:.2f} °C".format(temperature))
    board.displayShow(temperature)

    # Save data to a JSON file
    save_data_to_json(humidity, temperature)

    # Append the current data to the list
    data_entries.append({
        "humidity": humidity,
        "temperature": temperature
    })

    # Keep only the last 10 entries
    if len(data_entries) > MAX_DATA_ENTRIES:
        data_entries.pop(0)

def save_data_to_json(humidity, temperature):
    data = {
        "humidity": humidity,
        "temperature": temperature
    }
    with open("sensor_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("Data saved to sensor_data.json")

if __name__ == "__main__":
    setup()
    try:
        while True:
            loop()
            time.sleep(60)  # Wait for 1 minute before the next save
    except KeyboardInterrupt:
        print('Shutdown')
        board.shutdown()
        sys.exit(0)
        