# ZenoPay/client.py
import requests
from .utils import log_error

class ZenoPay:
    def __init__(self, account_id, api_key, secret_key, base_url="https://api.zeno.africa"):
        self.account_id = account_id
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

    def create_order(self, buyer_email, buyer_name, buyer_phone, amount):
        order_data = {
            'create_order': 1,
            'buyer_email': buyer_email,
            'buyer_name': buyer_name,
            'buyer_phone': buyer_phone,
            'amount': amount,
            'account_id': self.account_id,
            'api_key': self.api_key,
            'secret_key': self.secret_key
        }

        try:
            response = requests.post(self.base_url, data=order_data)
            response.raise_for_status()
            response_data = response.json()

            if response_data.get('status') == 'success':
                return {"success": True, "order_id": response_data.get('order_id')}
            else:
                return {"success": False, "message": response_data.get('message')}

        except requests.exceptions.HTTPError as http_err:
            log_error(f"HTTP error occurred: {http_err}")
            return {"success": False, "message": str(http_err)}
        except requests.exceptions.RequestException as req_err:
            log_error(f"Request error occurred: {req_err}")
            return {"success": False, "message": str(req_err)}

