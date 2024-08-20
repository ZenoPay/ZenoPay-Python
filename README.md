# ZenoPay

ZenoPay is a Python package for interacting with the Zeno Africa API.

## Installation

```bash
pip install ZenoPay


from ZenoPay import ZenoPay

# Initialize the client
zeno = ZenoPay(account_id="your_account_id", api_key="your_api_key", secret_key="your_secret_key")

# Create an order
response = zeno.create_order(
    buyer_email="customer@gmail.com",
    buyer_name="John Doe",
    buyer_phone="0744963858",
    amount=1000
)

if response["success"]:
    print(f"Order created successfully! Order ID: {response['order_id']}")
else:
    print(f"Order creation failed: {response['message']}")




### 6. Final Steps
1. **Install your package locally**: Run `pip install -e .` in the root directory where `setup.py` is located.
2. **Test your package**: Run your tests with `python -m unittest discover`.
3. **Publish**: If everything works, you can publish your package to PyPI.

This structure will give you a reusable package for interacting with the Zeno Africa API.
# ZenoPay-Python
