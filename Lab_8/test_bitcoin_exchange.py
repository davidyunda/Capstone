import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin_exchange

class Bitcoin_Exchange(TestCase):

    @patch('builtins.input', side_effect=['3'])
    def test_user_input_bitcoin(self, mock_input):
        answer = bitcoin_exchange.user_input_bitcoin()
        self.assertEqual(3, answer)

    @patch('bitcoin_exchange.get_API_bitcoin')
    def test_bitcoin_to_dollar(self, mock_rates):
        mock_rate = 30000
        api_response = {"time":{"updated":"Feb 27, 2022 14:46:00 UTC","updatedISO":"2022-02-27T14:46:00+00:00","updateduk":"Feb 27, 2022 at 14:46 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":38948.1695,"description":"United States Dollar","rate_float":mock_rate},"GBP":{"code":"GBP","symbol":"&pound;","rate":"29,049.5312","description":"British Pound Sterling","rate_float":29049.5312},"EUR":{"code":"EUR","symbol":"&euro;","rate":"34,553.0243","description":"Euro","rate_float":34553.0243}}}
        mock_rates.side_effect = [ api_response ]
        converted = bitcoin_exchange.bitcoin_to_dollar(3)
        self.assertEqual(90000, converted)

    @patch('builtins.print')
    def test_display_results(self, mock_print):
        bitcoin_exchange.display_results(3, 90000)
        mock_print.assert_called_once_with('3 Bitcoin is equivalent to $90000.00')

    def test_convert_bitcoin_to_dollars(self):
        price = bitcoin_exchange.convert_bitcoin_to_dollars(3, 30000)
        self.assertEqual(90000, price)

if __name__ == '__main__':
    unittest.main()
