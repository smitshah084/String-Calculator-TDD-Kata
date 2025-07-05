import unittest
from calculator import add

class TestStringCalculator(unittest.TestCase):
    
    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)
        
    def test_one_number_input(self):
        self.assertEqual(add("1"),1)
        
    def test_two_number_input(self):
        self.assertEqual(add("1,1"),2)