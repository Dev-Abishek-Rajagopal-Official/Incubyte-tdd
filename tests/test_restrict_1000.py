"""
Unit tests for the StringCalculator class.
"""

from calculator.calc import StringCalculator

calc = StringCalculator()

def test_ignore_numbers_greater_than_1000_1():
    """
    Test that numbers greater than 1000 are ignored.
    """
    assert calc.add("2,1001") == 2

def test_ignore_numbers_greater_than_1000_2():
    """
    Test that multiple numbers greater than 1000 are ignored.
    """
    assert calc.add("2,1001,20000,3") == 5