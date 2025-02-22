from calculator.calc import StringCalculator

calc = StringCalculator()

def test_ignore_numbers_greater_than_1000_1():
    assert calc.add("2,1001") == 2

def test_ignore_numbers_greater_than_1000_2():
    assert calc.add("2,1001,20000,3") == 5