# String-Calculator-TDD-Kata
String Calculator Kata using Test-Driven Development. Demonstrates clean code practices, unit testing, and incremental development.

## ✅ TDD Cycle Followed

This project followed the classic **Red → Green → Refactor** cycle:

1. Write a failing test
2. Write the minimal code to make the test pass
3. Refactor while keeping tests green

### 🛠️ Dependencies

This project is developed using **Python’s built-in `unittest` framework**, so there are **no external libraries required** to run the tests.

## 🚀 Features Implemented

1. Returns `0` for an empty string.
2. Returns the number itself for a single number input.
3. Adds two comma-separated numbers.
4. Handles an unknown amount of comma-separated numbers.
5. Handles newline characters (`\n`) as delimiters.
6. Supports custom delimiters (e.g., `//;\n1;2`).
7. Throws an exception for negative numbers with all negatives listed.
8. Ignores numbers greater than `1000`.
9. Supports delimiters of any length (e.g., `//[***]\n1***2***3`).
10. Supports multiple delimiters (e.g., `//[*][%]\n1*2%3`).
11. Supports multiple delimiters of any length (e.g., `//[***][##][@@]\n1***2##3@@4`).


## Test Cases
```python    
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
```

## 🖼️ Screenshots


### Test Results
![Test Results](/Screenshots/result.png?raw=true "Test Results")



#### ✅ Requirements

* **Python 3.7+**

You can check your Python version with:

```bash
python --version
```

#### 🧪 Running the Tests

No extra setup is needed. Simply run the following command:

```bash
python main.py
```

```
string-calculator/
├── calculator/                 # Package for the main logic
│   ├── __init__.py
│   └── string_calculator.py    # calculator functions
│
├── tests/                      # Unit tests
│   ├── __init__.py
│   └── test_string_calculator.py
|
├── Screenshots
├── LICENSE                     # MIT or other license
├── README.md
├── requirements.txt            # Dependencies (e.g., unittest)
└── .gitignore                  # Ignore __pycache__, .env, etc.
```
