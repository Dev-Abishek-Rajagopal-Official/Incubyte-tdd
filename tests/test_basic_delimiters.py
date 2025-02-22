"""
Unit tests for the StringCalculator class.
"""

from calculator.calc import StringCalculator

def test_sum_delimitor_1():
    """
    Test that the calculator correctly adds numbers separated by a comma.
    """
    calc = StringCalculator()
    assert calc.add("1,2") == 3

def test_sum_delimitor_2():
    """
    Test that the calculator correctly adds numbers separated by a pipe (|).
    """
    calc = StringCalculator()
    assert calc.add("1|2") == 3

def test_sum_delimitor_3():
    """
    Test that the calculator correctly adds numbers separated by a newline (\n).
    """
    calc = StringCalculator()
    assert calc.add("1\n2") == 3

def test_sum_delimitor_all():
    """
    Test that the calculator correctly adds numbers separated by a mix of delimiters:
    comma (,), pipe (|), and newline (\n).
    """
    calc = StringCalculator()
    assert calc.add("1,2|3\n5") == 11
