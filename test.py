import requests
import json
import os
from datetime import datetime

# Define API parameters
TICKER = "AAPL"
START_DATE = "2025-02-26"
END_DATE = "2025-02-28"
API_KEY = "Mbotb9f_zwSo7fofFJeQwKZb42rjNprk"  # Replace with your API key

# API URL
API_URL = f"https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/1/day/{START_DATE}/{END_DATE}?adjusted=true&sort=asc&apiKey={API_KEY}"

# Fetch data from API
response = requests.get(API_URL)

# Check for errors
if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    exit()

# Parse response JSON
data = response.json()

# Define save location
SAVE_DIR = os.path.expanduser("~/Documents/polygon_data")  # Change this to your preferred directory
os.makedirs(SAVE_DIR, exist_ok=True)

# Generate filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"{TICKER}_data_{timestamp}.json"
file_path = os.path.join(SAVE_DIR, file_name)

# Save JSON file locally
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data saved successfully: {file_path}")
