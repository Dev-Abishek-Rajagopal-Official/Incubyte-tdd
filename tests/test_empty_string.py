from calculator.calc import StringCalculator

def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0
