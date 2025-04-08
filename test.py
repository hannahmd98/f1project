import requests
import pandas as pd

def find_driver_numbers(data):
    """Recursively search for 'driver_number' in nested JSON data."""
    driver_numbers = set()
    
    # If data is a list, iterate through each item
    if isinstance(data, list):
        for item in data:
            driver_numbers.update(find_driver_numbers(item))
    
    # If data is a dictionary, check each key-value pair
    elif isinstance(data, dict):
        for key, value in data.items():
            if key == 'driver_number':
                driver_numbers.add(value)  # Found driver number, add to set
            else:
                driver_numbers.update(find_driver_numbers(value))  # Recurse into nested structure
    
    return driver_numbers

def get_driver_numbers():
    """Fetch distinct driver numbers from the drivers endpoint."""
    url = "https://api.openf1.org/v1/drivers"
    headers = {'User-Agent': 'f1_test'}

    try:
        response = requests.get(url, headers=headers, timeout=60)
        response.raise_for_status()
        
        driver_data = response.json()
        # Recursively search for 'driver_number' in the fetched data
        driver_numbers = list(find_driver_numbers(driver_data))
        
        #print("Available distinct driver numbers:", driver_numbers)
        return driver_numbers

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch driver numbers: {e}")
        return []

# Usage example
driver_numbers = get_driver_numbers()