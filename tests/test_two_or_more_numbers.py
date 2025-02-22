from calculator.calc import StringCalculator

def test_two_string():
    calc = StringCalculator()
    assert calc.add("1,2") == 3

def test_more_than_two_string():
    calc = StringCalculator()
    assert calc.add("100,200,300,500,1000") == 2100
