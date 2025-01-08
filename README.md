
## ZenoPay Documentation for Order Creating , USSD Payment and Webhook

The script you've provided outlines how to handle order creation, USSD payment, and webhook integration for a payment system. Below is a breakdown of the important steps and additions that you can implement:

### 1. **Creating the Order and Pushing USSD Payment**

You will be sending a POST request to the endpoint `https://api.zeno.africa`, and in your case, you're including metadata. Here's an example of how metadata is added to the request:

- **Metadata Format:** 
  - The metadata is serialized into a JSON format and included as a string. This allows you to store additional information about the order such as `product_id`, `color`, `size`, and `custom_notes`.

```python
import requests
import json

# URL of the API endpoint
url = "https://apigw.zeno.africa/mapenzi.php"

# Data to send for creating the order and pushing USSD payment
order_data = {
    "create_order": 1,
    "buyer_email": "jackson@gmail.com",
    "buyer_name": "dastani",
    "buyer_phone": "0652449389",
    "amount": 1000,
    "webhook_url": "https://yourwebsite.com/webhook",
    "account_id": "zp87778",
    "metadata": json.dumps({
        "product_id": "12345",
        "color": "blue",
        "size": "L",
        "custom_notes": "Please gift-wrap this item."
    }),
    "api_key": "null",
    "secret_key": "null"
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

This section is used to check the status of an order by sending a POST request to `https://api.zeno.africa/order-status`. You can use the following approach to fetch and display the order status.

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

### 3. **Webhook Handler**

To handle incoming webhook notifications, you can set up an endpoint on your server that listens for `POST` requests. Here's a simple Flask example:

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
```

### **Summary of the Workflow**
1. **Order Creation:** You create an order using a `POST` request, including the buyer’s details, payment information, and any additional metadata that may be required.
2. **Order Status Check:** To check the status of the order, send a `POST` request with the `order_id`.
3. **Webhook Setup:** The server should be prepared to handle webhook notifications that update the system about the payment status or any changes in the order.

This approach will ensure your payment process works smoothly with metadata included, handling order creation, status checking, and webhooks effectively.
