# String Calculator

## Overview
The **String Calculator** is a simple utility that takes a string of numbers separated by delimiters and returns their sum. It supports various delimiters, including custom ones, and provides error handling for negative numbers and number restrictions.

## Features
- Supports default delimiters: `,`, `|`, and `\n`
- Allows custom delimiters using `//[delimiter]\n` notation
- Supports multiple custom delimiters
- Handles delimiters of any length
- Raises an exception for negative numbers
- Ignores numbers greater than 1000

## Project Structure
```
string-calculator/
│── calculator/
│   ├── __init__.py
│   ├── calc.py          # Implementation of StringCalculator class
│
│── tests/
│   ├── test_basic_delimiters.py         # Tests for default delimiters
│   ├── test_custom_delimiters.py        # Tests for custom delimiters
│   ├── test_empty_string.py             # Tests for empty string input
│   ├── test_negative_value_exception.py  # Tests for negative number handling
│   ├── test_restrict_1000.py            # Tests for ignoring numbers > 1000
│   ├── test_single_number.py            # Tests for a single number input
│   ├── test_two_or_more_numbers.py      # Tests for multiple numbers
│
│── README.md         # Project documentation
│── pytest.ini        # Pytest configuration
```

## Usage
To use the `StringCalculator`, instantiate the class and call the `add` method:
```python
from calculator.calc import StringCalculator

calc = StringCalculator()
result = calc.add("1,2,3")
print(result)  # Output: 6
```

## Running Tests
To run the test suite, execute the following command:
```sh
pytest tests/
```
This will execute all test cases and display the results.

## Dependencies
- Python 3.10
- Pytest 8.3


