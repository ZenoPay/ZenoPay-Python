import requests
import json

# URL of the API endpoint
url = "https://api.zeno.africa/status"

def check_order_status(order_id):
    # Data to send for checking the order status
    status_data = {
        'check_status': 1,
        'order_id': order_id,
        'api_key': 'YOUR API',
        'secret_key': 'YOUR SECRET KEY'
    }

    try:
        # Send POST request to check the order status
        response = requests.post(url, data=status_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the response as JSON
    except requests.RequestException as e:
        log_error(f"Error fetching order status: {e}")
        return {
            'success': False,
            'message': 'Error fetching order status'
        }

def log_error(message):
    # Function to log errors
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"{message}\n")

def show_response(response):
    # Function to display the response
    print(json.dumps(response, indent=2))

# Order ID to check
order_id = '66c4bb9c9abb1'

# Get the order status
response = check_order_status(order_id)

# Show the response
show_response(response)
