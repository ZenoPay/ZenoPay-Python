import requests
import json

# ZenoPay API endpoint for Mobile Money Tanzania
API_URL = "https://zenoapi.com/api/payments/mobile_money_tanzania"

# Your API Key (store securely in production)
API_KEY = "YOUR_API_KEY"

# Payment order payload
payload = {
    "order_id": "your-unique-order-id",  # e.g., UUID
    "buyer_email": "customer@example.com",
    "buyer_name": "John Doe",
    "buyer_phone": "0752117588",  # Tanzanian format: 07XXXXXXXX
    "amount": 10000,  # Amount in TZS
    "webhook_url": "https://yourdomain.com/payment-webhook"  # Optional but recommended
}

# Request headers with API key
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

try:
    # Send POST request
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    # Parse JSON response
    data = response.json()
    print("ZenoPay Response:")
    print(json.dumps(data, indent=4))

except requests.exceptions.HTTPError as http_err:
    print(f"[HTTP ERROR] {http_err}")
except requests.exceptions.ConnectionError:
    print("[CONNECTION ERROR] Failed to connect to ZenoPay API.")
except requests.exceptions.Timeout:
    print("[TIMEOUT ERROR] Request timed out.")
except requests.exceptions.RequestException as e:
    print(f"[REQUEST ERROR] {e}")
