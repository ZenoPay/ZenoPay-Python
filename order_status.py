import requests
import json

# --- Configuration ---
API_KEY = "YOUR_API_KEY"
ORDER_ID = "66c4bb9c9abb1"

# ZenoPay Order Status endpoint
API_URL = f"https://zenoapi.com/api/payments/order-status?order_id={ORDER_ID}"

# Request headers
headers = {
    "x-api-key": API_KEY
}

try:
    # Send GET request
    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()

    # Parse JSON response
    data = response.json()

    # Check if the response was successful
    if data.get("resultcode") == "000":
        order_info = data.get("data", [])[0]  # First result in the list

        result = {
            "status": "success",
            "order_id": order_info.get("order_id"),
            "payment_status": order_info.get("payment_status"),
            "amount": order_info.get("amount"),
            "channel": order_info.get("channel"),
            "reference": order_info.get("reference"),
            "msisdn": order_info.get("msisdn"),
            "message": data.get("message")
        }
    else:
        result = {
            "status": "error",
            "message": data.get("message", "Unable to fetch order status")
        }

except requests.exceptions.HTTPError as http_err:
    result = {"status": "error", "message": f"HTTP error: {http_err}"}
except requests.exceptions.ConnectionError:
    result = {"status": "error", "message": "Connection error."}
except requests.exceptions.Timeout:
    result = {"status": "error", "message": "Request timed out."}
except requests.exceptions.RequestException as err:
    result = {"status": "error", "message": f"Request error: {err}"}

# Print final result
print(json.dumps(result, indent=4))
