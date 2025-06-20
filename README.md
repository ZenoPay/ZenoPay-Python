

## ✅ ZenoPay API Integration Guide – Order Creation, USSD Payment, and Webhook Handling

This guide provides Python-based code examples to integrate with ZenoPay's Mobile Money Tanzania API, enabling:

1. **Order Creation & USSD Push**
2. **Order Status Check**
3. **Webhook Notification Handling**

---

### 🔹 1. Create Order & Initiate Mobile Money (USSD Push)

> **Endpoint:** `https://zenoapi.com/api/payments/mobile_money_tanzania`
> **Method:** `POST`
> **Authentication:** Use `x-api-key` in the request header

```python
import requests
import json
import uuid

# --- ZenoPay API Config ---
API_URL = "https://zenoapi.com/api/payments/mobile_money_tanzania"
API_KEY = "YOUR_API_KEY"

# --- Unique Order ID (UUID recommended) ---
order_id = str(uuid.uuid4())

# --- Payload for order creation with metadata ---
payload = {
    "order_id": order_id,
    "buyer_email": "jackson@gmail.com",
    "buyer_name": "Dastani",
    "buyer_phone": "0652449389",  # Format: 07XXXXXXXX
    "amount": 1000,  # Amount in TZS
    "webhook_url": "https://yourdomain.com/webhook",
    "metadata": {
        "product_id": "12345",
        "color": "blue",
        "size": "L",
        "custom_notes": "Please gift-wrap this item."
    }
}

# --- Headers including API Key ---
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

# --- Send POST Request ---
try:
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    print("✅ Order Submitted Successfully:")
    print(json.dumps(response.json(), indent=4))

except requests.RequestException as e:
    print(f"❌ Failed to create order: {e}")
```

---

### 🔹 2. Check Order Status

> **Endpoint:** `https://zenoapi.com/api/payments/order-status`
> **Method:** `GET`
> **Parameters:** `order_id` in query string
> **Authentication:** `x-api-key` header

```python
import requests
import json

# --- Config ---
API_KEY = "YOUR_API_KEY"
ORDER_ID = "66c4bb9c9abb1"

# --- Request URL ---
url = f"https://zenoapi.com/api/payments/order-status?order_id={ORDER_ID}"

# --- Headers ---
headers = {
    "x-api-key": API_KEY
}

# --- GET Request to check order status ---
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    if data.get("resultcode") == "000":
        order = data["data"][0]
        print("✅ Order Status:")
        print(json.dumps({
            "order_id": order["order_id"],
            "payment_status": order["payment_status"],
            "amount": order["amount"],
            "channel": order["channel"],
            "msisdn": order["msisdn"],
            "reference": order["reference"],
            "created": order["creation_date"]
        }, indent=4))
    else:
        print(f"❌ Failed: {data.get('message')}")

except requests.RequestException as e:
    print(f"❌ Error: {e}")
```

---

### 🔹 3. Webhook Listener for Payment Status Updates

> ZenoPay will call your `webhook_url` when a payment is marked `COMPLETED`. The webhook payload includes metadata and transaction details.

```python
from flask import Flask, request
import datetime
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        # Parse JSON payload
        payload = request.json

        # Log payload to file with timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('weblogs.txt', 'a') as log_file:
            log_file.write(f"[{timestamp}] Webhook Received:\n")
            log_file.write(json.dumps(payload, indent=2) + "\n")

        return 'Webhook received', 200

    except Exception as e:
        return f'Webhook error: {e}', 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

#### 📥 Example Webhook Payload

```json
{
  "order_id": "677e43274d7cb",
  "payment_status": "COMPLETED",
  "reference": "1003020496",
  "metadata": {
    "product_id": "12345",
    "color": "blue",
    "size": "L",
    "custom_notes": "Please gift-wrap this item."
  }
}
```

---

### ✅ Summary: Full Payment Flow

| Step                 | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| Order Creation       | Submit buyer info, amount, metadata, and webhook URL       |
| USSD Push            | Payment is initiated to buyer's mobile via USSD            |
| Order Status Check   | Use `GET` request to check payment status                  |
| Webhook Notification | Receive updates to your server once payment is `COMPLETED` |

---

