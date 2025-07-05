import unittest
from calculator import add

class TestStringCalculator(unittest.TestCase):
    
    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)
        
    