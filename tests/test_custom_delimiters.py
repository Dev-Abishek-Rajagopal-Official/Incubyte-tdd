from calculator.calc import StringCalculator

calc = StringCalculator()

def test_custom_delimiter():
    assert calc.add("//;\n1;2") == 3

def test_multiple_custom_delimiters():
    assert calc.add("//[*][%]\n1*2%3") == 6

def test_custom_delimiters_of_any_length():
    assert calc.add("//[***]\n1***2***3") == 6

def test_multiple_delimiters_of_any_length():
    assert calc.add("//[**][%%]\n1**2%%3") == 6