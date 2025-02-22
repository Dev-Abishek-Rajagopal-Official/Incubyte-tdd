"""
Unit tests for the StringCalculator class.
"""

from calculator.calc import StringCalculator

calc = StringCalculator()

def test_empty_string():
    """
    Test that the calculator returns 0 for an empty string.
    """
    assert calc.add("") == 0