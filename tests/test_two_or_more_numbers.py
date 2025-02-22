"""
Unit tests for the StringCalculator class.
"""

from calculator.calc import StringCalculator

calc = StringCalculator()

def test_two_string():
    """
    Test that the calculator correctly handles two numbers separated by a comma.
    """
    assert calc.add("1,2") == 3

def test_more_than_two_string():
    """
    Test that the calculator correctly handles more than two numbers separated by commas.
    """
    assert calc.add("100,200,300,500,1000") == 2100
