import requests

# URL of the API endpoint
url = "https://api.zeno.africa"

# Data to send for creating the order
order_data = {
    'create_order': 1,
    'buyer_email': 'YOUR_CUSTOMER_EMAIL',
    'buyer_name': 'YOUR_CUSTOMER_NAME',
    'buyer_phone': '0752117588',
    'amount': 10000,
    'account_id': 'YOUR_ACCOUNT_ID',
    'api_key': 'YOUR_KEY',
    'secret_key': 'YOUR_SECRET_KEY'
}

try:
    # Send POST request to create the order
    response = requests.post(url, data=order_data)
    
    # Print the response
    print(response.text)

except requests.RequestException as e:
    # Log errors to a file
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"Error: {e}\n")
