
## Documentation for ZenoPay

### Script 1: Create an Order via API

#### Overview
This Python script demonstrates how to interact with an API to create an order. It sends a POST request to the specified API endpoint with the necessary order data and handles any potential errors by logging them to a file.

#### Requirements
- Python 3.x
- `requests` library (install via `pip install requests`)

#### Script Breakdown

##### 1. Import Required Library
```python
import requests
```
- **requests**: A popular Python library for making HTTP requests, simplifying operations like GET and POST.

##### 2. Define the API Endpoint
```python
# URL of the API endpoint
url = "https://api.zeno.africa"
```
- **url**: The API endpoint for creating an order.

##### 3. Prepare the Order Data
```python
# Data for creating the order
order_data = {
    'create_order': 1,
    'buyer_email': 'customer@gmail.com',
    'buyer_name': 'John Doe',
    'buyer_phone': '0752117588',
    'amount': 10000,
    'account_id': 'YOUR_ACCOUNT_ID',
    'api_key': 'YOUR_KEY',
    'secret_key': 'YOUR_SECRET_KEY'
}
```
- **order_data**: Dictionary containing the necessary order information, including buyer details, order amount, and authentication keys.

##### 4. Send the POST Request
```python
try:
    # Send POST request to create the order
    response = requests.post(url, data=order_data)
    
    # Print the response
    print(response.text)
except requests.RequestException as e:
    # Log errors to a file
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"Error: {e}\n")
```
- **requests.post(url, data=order_data)**: Sends a POST request with `order_data` to the specified `url`.
- **response.text**: Displays the server's response.
- **try-except block**: Handles exceptions and logs errors to `error_log.txt`.

#### Usage
1. Ensure Python is installed on your machine.
2. Install the `requests` library:
   ```bash
   pip install requests
   ```
3. Update `order_data` with actual values.
4. Run the script:
   ```bash
   python create_order.py
   ```
5. Check the terminal for the response.
6. Errors will be logged in `error_log.txt`.

---

### Script 2: Check Payment Status via API

#### Overview
This Python script checks the status of a payment by sending a POST request to an API endpoint with the order ID and authentication credentials. It processes the response and handles errors by logging them to a file.

#### Requirements
- Python 3.x
- `requests` library (install via `pip install requests`)

#### Script Breakdown

##### 1. Import Required Libraries
```python
import requests
import json
```
- **requests**: Library for sending HTTP requests.
- **json**: Library for handling JSON data.

##### 2. Define the API Endpoint
```python
# URL of the API endpoint
url = "https://api.zeno.africa/status"
```
- **url**: The API endpoint for checking payment status.

##### 3. Define Function to Check Payment Status
```python
def check_order_status(order_id):
    # Data for checking the order status
    status_data = {
        'check_status': 1,
        'order_id': order_id,
        'api_key': 'YOUR_API_KEY',
        'secret_key': 'YOUR_SECRET_KEY'
    }

    try:
        # Send POST request to check order status
        response = requests.post(url, data=status_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the response as JSON
    except requests.RequestException as e:
        log_error(f"Error fetching order status: {e}")
        return {
            'success': False,
            'message': 'Error fetching order status'
        }
```
- **check_order_status(order_id)**: Sends a POST request to check the status of an order.
  - **status_data**: Contains the required fields including `order_id`, `api_key`, and `secret_key`.
  - **requests.post(url, data=status_data)**: Sends the POST request.
  - **response.raise_for_status()**: Raises an exception for HTTP errors.
  - **response.json()**: Returns the response in JSON format.
  - **log_error()**: Logs exceptions.

##### 4. Define Function to Log Errors
```python
def log_error(message):
    # Log errors to a file
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"{message}\n")
```
- **log_error(message)**: Appends error messages to `error_log.txt`.

##### 5. Define Function to Display the Response
```python
def show_response(response):
    # Display the response in a pretty-printed JSON format
    print(json.dumps(response, indent=2))
```
- **show_response(response)**: Formats and prints the response as JSON.

##### 6. Main Code
```python
# Order ID to check
order_id = '66c4bb9c9abb1'

# Get the order status
response = check_order_status(order_id)

# Display the response
show_response(response)
```
- **order_id**: The ID of the order to check.
- **check_order_status(order_id)**: Retrieves the status.
- **show_response(response)**: Displays the result.

#### Usage
1. Ensure Python is installed on your system.
2. Install the `requests` library:
   ```bash
   pip install requests
   ```
3. Replace `'YOUR_API_KEY'` and `'YOUR_SECRET_KEY'` with your actual API credentials.
4. Update the `order_id` variable with the ID of the order to check.
5. Run the script:
   ```bash
   python check_payment_status.py
   ```
6. Check the terminal for the response.
7. Errors will be logged in `error_log.txt`.

#### Notes
- Handle sensitive information like API keys and secret keys securely and avoid exposing them in public repositories.
- Update `url` and data structures based on actual API specifications.

--- 
