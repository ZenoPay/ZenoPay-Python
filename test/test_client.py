# tests/test_client.py
import unittest
from ZenoPay.client import ZenoPay

class TestZenoPay(unittest.TestCase):
    def setUp(self):
        self.zeno = ZenoPay(account_id="zp87778", api_key="6471f68e74b687fe93722f9d50896386", secret_key="f60464a551d412da8241fa460da9e6777543c14ca19688bc26a3a2d79bae848b")

    def test_create_order(self):
        result = self.zeno.create_order(buyer_email="customer@gmail.com", buyer_name="John Doe", buyer_phone="0744963858", amount=1000)
        self.assertIn("success", result)

if __name__ == "__main__":
    unittest.main()
