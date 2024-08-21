import requests

# The endpoint URL where the request will be sent
endpoint_url = "https://api.zeno.africa/order-status"

# Order ID that you want to check the status for
order_id = "66c4bb9c9abb1"

# Data to be sent in the POST request
post_data = {
    'check_status': 1,
    'order_id': order_id,
    'api_key': 'YOUR API',
    'secret_key': 'YOUR SECRET KEY'
}

try:
    # Send the POST request
    response = requests.post(endpoint_url, data=post_data)

    # Check if the request was successful
    response.raise_for_status()

    # Decode the JSON response
    response_data = response.json()

    # Format the response to match the desired structure
    if response_data['status'] == 'success':
        result = {
            "status": "success",
            "order_id": response_data['order_id'],
            "message": response_data['message'],
            "payment_status": response_data.get('payment_status')
        }
    else:
        result = {
            "status": "error",
            "message": response_data['message']
        }

except requests.exceptions.RequestException as e:
    result = {
        "status": "error",
        "message": f'Request error: {str(e)}'
    }

# Print the result in JSON format
print(result)
