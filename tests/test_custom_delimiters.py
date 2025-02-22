"""
Unit tests for the StringCalculator class.
"""

from calculator.calc import StringCalculator

calc = StringCalculator()

def test_custom_delimiter():
    """
    Test that the calculator correctly handles a single custom delimiter.
    """
    assert calc.add("//;\n1;2") == 3

def test_multiple_custom_delimiters():
    """
    Test that the calculator correctly handles multiple custom delimiters.
    """
    assert calc.add("//[*][%]\n1*2%3") == 6

def test_custom_delimiters_of_any_length():
    """
    Test that the calculator correctly handles custom delimiters of any length.
    """
    assert calc.add("//[***]\n1***2***3") == 6

def test_multiple_delimiters_of_any_length():
    """
    Test that the calculator correctly handles multiple custom delimiters of any length.
    """
    assert calc.add("//[**][%%]\n1**2%%3") == 6
