import unittest
from unittest import TestCase
import camel_case

class Camel_Case(TestCase):

    def test_camel_case_sentence(self):
        self.assertEqual('helloWorld', camel_case.camel_case('Hello World'))

    def test_single_word(self):
        self.assertEqual('hello', camel_case.camel_case('Hello'))

    def test_with_more_than_two_words(self):
        self.assertEqual('todayWeWillBeLearningANewLanguage', camel_case.camel_case('today we will be learning a new language'))

    def test_with_empty_strings(self):
        self.assertEqual('', camel_case.camel_case('   '))

if __name__ == '__main__':
    unittest.main()