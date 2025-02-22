from calculator.calc import StringCalculator

def test_single_string():
    calc = StringCalculator()
    assert calc.add("1") == 1
