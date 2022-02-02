import unittest
from unittest import TestCase
import camel_case

class Camel_Case(TestCase):
    def test_camel_case_sentence(self):
        self.assertEqual('helloWorld', camel_case.camel_case('Hello World'))

if __name__ == '__main__':
    unittest.main()