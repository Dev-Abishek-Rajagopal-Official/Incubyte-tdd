"""
Unit tests for the StringCalculator class.
"""

from calculator.calc import StringCalculator

calc = StringCalculator()

def test_single_string():
    """
    Test that the calculator correctly handles a single number input.
    """
    assert calc.add("1") == 1
