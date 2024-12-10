import unittest
from aangaraa_pay.payment import AangaraaPay

class TestAangaraaPay(unittest.TestCase):
    def setUp(self):
        self.payment = AangaraaPay('https://your-api-url.com/api', 'your_app_key')

    def test_initiate_payment(self):
        response = self.payment.initiate_payment('237600000000', 1000, 'Test Payment', 'unique_transaction_id', 'MTN_Cameroon')
        self.assertIn('status', response)

if __name__ == '__main__':
    unittest.main()
