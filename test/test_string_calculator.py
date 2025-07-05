import unittest
import random
from calculator import add

class TestStringCalculator(unittest.TestCase):
    
    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)
        
    def test_one_number_input(self):
        self.assertEqual(add("1"),1)
        
    def test_two_number_input(self):
        self.assertEqual(add("1,1"),2)
        
    def test_n_number_input(self):
        self.assertEqual(add("1,3,3432,13"),17)
        numbers = [random.randint(0, 100) for _ in range(20)]
        input_str = ",".join(map(str, numbers))
        self.assertEqual(add(input_str), sum(numbers))
        
    def test_slash_n_delimiter(self):
        self.assertEqual(add("1\n3"),4)
        
    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;43;23"),67)
        
    def test_negative_number_input(self):
        with self.assertRaises(ValueError) as context:
            add("-3,4")
        
        self.assertIn(f"negative numbers not allowed {-3}", str(context.exception))
        
    def test_number_greeater_than_1000_input(self):
        self.assertEqual(add("10234,32"),32)
        
    def test_custom_delimeter_of_any_length(self):
        self.assertEqual(add('//[***]\n1***2***3'),6)
        
    def test_allow_multiple_delimeters(self):
        self.assertEqual(add("//[*][%]\n1*2%3"),6)
        
    def test_multiple_delimiters_with_length_longer_than_one(self):
        self.assertEqual(add("//[***][%]\n1***2%3"),6)