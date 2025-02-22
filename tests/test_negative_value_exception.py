"""
Unit tests for the StringCalculator class.
"""

import pytest

from calculator.calc import StringCalculator

calc = StringCalculator()

def test_negative_numbers():
    """
    Test that the calculator raises a ValueError when negative numbers are included.
    """
    with pytest.raises(ValueError, match=r"Negatives not allowed: -1"):
        calc.add("1,-1,2")

def test_multiple_negative_numbers():
    """
    Test that the calculator raises a ValueError listing all negative numbers.
    """
    with pytest.raises(ValueError, match=r"Negatives not allowed: -1, -3, -5"):
        calc.add("1,-1,2,-3,-5")