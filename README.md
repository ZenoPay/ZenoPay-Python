
## ZenoPay Documentation for Order Creating , USSD Payment and Webhook

### 1. **Creating an Order and Pushing USSD Payment**

To create an order and initiate USSD payment, you need to send a POST request to the endpoint. Here’s how to handle it:

**API Endpoint:**
```
POST https://api.zeno.africa
```

**Request Data:**
```python
{
    'buyer_email': 'YOUR_CUSTOMER_EMAIL',
    'buyer_name': 'YOUR_CUSTOMER_NAME',
    'buyer_phone': '0752117588',
    'amount': 10000,
    'account_id': 'YOUR_ACCOUNT_ID',
    'webhook_url': 'your webhook url',
    'api_key': 'YOUR_API_KEY',
    'secret_key': 'YOUR_SECRET_KEY',
}
```

**Example Python Code:**
```python
import requests

# URL of the API endpoint
url = "https://api.zeno.africa"

# Data to send for creating the order and pushing USSD payment
order_data = {
    'create_order': 1,
    'buyer_email': 'YOUR_CUSTOMER_EMAIL',
    'buyer_name': 'YOUR_CUSTOMER_NAME',
    'buyer_phone': '0752117588',
    'amount': 10000,
    'webhook_url': 'your webhook url',
    'account_id': 'YOUR_ACCOUNT_ID',
    'api_key': 'YOUR_API_KEY',
    'secret_key': 'YOUR_SECRET_KEY',
}

try:
    # Send POST request to create the order and initiate USSD payment
    response = requests.post(url, data=order_data)
    
    # Print the response
    print(response.text)

except requests.RequestException as e:
    # Log errors to a file
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"Error: {e}\n")
```

### 2. **Checking Order Status**

To check the status of an order, you need to send a POST request to the status checking endpoint.

**API Endpoint:**
```
POST https://api.zeno.africa/order-status
```

**Request Data:**
```python
{
    'check_status': 1,
    'order_id': 'ORDER_ID',
    'api_key': 'YOUR_API_KEY',
    'secret_key': 'YOUR_SECRET_KEY'
}
```

**Example Python Code:**
```python
import requests
import json

# URL of the API endpoint
url = "https://api.zeno.africa/order-status"

def check_order_status(order_id):
    # Data to send for checking the order status
    status_data = {
        'check_status': 1,
        'order_id': order_id,
        'api_key': 'YOUR_API_KEY',
        'secret_key': 'YOUR_SECRET_KEY'
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
```

**Sample Response:**
```json
{
    "status": "success",
    "order_id": "66c0e338e82b3",
    "message": "Order status updated",
    "payment_status": "PENDING"
}
```

### 3. **Setting Up the Webhook**

To handle incoming webhook notifications, set up an endpoint on your server to receive and process POST requests.

**Example Webhook Handler in Python:**
```python
from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    if request.method == 'POST':
        # Get the raw POST data from the incoming webhook
        data = request.data.decode('utf-8')

        # Log the raw data with a timestamp
        with open('weblogs.txt', 'a') as log_file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"[{timestamp}] WebHook Data: {data}\n")

        return 'Webhook received', 200

if __name__ == '__main__':
    app.run(debug=True)


[2024-12-12 14:00:00] WebHook Data: {"order_id":"6757c69cddfa6","payment_status":"COMPLETED","reference":"0882061614"}


```

### Summary

- **Create an Order and Push USSD Payment:** Send a POST request to `https://api.zeno.africa` with order and payment details.
- **Check Order Status:** Send a POST request to `https://api.zeno.africa/order-status` with `order_id`.
- **Webhook Handling:** Set up an endpoint to receive and process webhook notifications.
