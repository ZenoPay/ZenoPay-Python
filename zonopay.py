import json
import requests
import time
import logging

class ZenoPay:
    def __init__(self, api_key, sandbox, webhook_url):
        self.api_key = api_key
        self.sandbox = sandbox
        self.endpoint = 'https://zeno.co.tz/api/v1/pay.php'  # Updated endpoint URL
        self.webhook_url = webhook_url
        self.logger = logging.getLogger(__name__)

    def make_payment(self, amount, transaction_id, phone_number, description):
        payload = {
            'api': 170,
            'code': 104,
            'data': {
                'api_key': self.api_key,
                'order_id': transaction_id,
                'amount': amount,
                'username': description,
                'is_live': not self.sandbox,
                'phone_number': phone_number,
                'webhook_url': self.webhook_url
            }
        }

        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(self.endpoint, json=payload, headers=headers)
            response.raise_for_status()  # Raise exception for bad status codes

            data = response.json()
            if data is None:
                self.logger.error('ZenoPay API call failed to get result. Response data is None.')
                raise Exception('ZenoPay API call failed to get result. Please check.')

            return data
        except requests.exceptions.RequestException as e:
            self.logger.error(f'ZenoPay API request failed: {e}')
            raise Exception(f'ZenoPay API request failed: {e}')
        except json.JSONDecodeError as e:
            self.logger.error(f'Error decoding JSON response: {e}')
            raise Exception(f'Error decoding JSON response: {e}')
        except Exception as e:
            self.logger.error(f'Unexpected error during ZenoPay API request: {e}')
            raise Exception(f'Unexpected error during ZenoPay API request: {e}')


def create_order_id():
    # Generate an order ID starting with 'Z' followed by the current timestamp
    return 'Z' + str(int(time.time()))

def create_order_and_request_payment():
    api_key = 'YOUR API KEY'  # Example API key
    sandbox = False  # Set to True for sandbox mode
    webhook_url = 'YOUR WEBHOOK URL '  # Webhook URL

    zeno_pay = ZenoPay(api_key, sandbox, webhook_url)
    
    # Generate a unique order ID
    order_id = create_order_id()
    amount = 10000  # Example amount
    description = f'Payment Description #{order_id}'
    
    # Predefined phone number (example)
    phone_number = '0652449389'

    try:
        # Make the payment request
        response = zeno_pay.make_payment(amount, order_id, phone_number, description)
        print(response)  # Response from the payment gateway

    except Exception as e:
        print(f'Failed to make payment: {e}')

if __name__ == "__main__":
    create_order_and_request_payment()
