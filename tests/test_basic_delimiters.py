from calculator.calc import StringCalculator

def test_sum_delimitor_1():
    calc = StringCalculator()
    assert calc.add("1,2") == 3

def test_sum_delimitor_2():
    calc = StringCalculator()
    assert calc.add("1|2") == 3

def test_sum_delimitor_3():
    calc = StringCalculator()
    assert calc.add("1\n2") == 3

def test_sum_delimitor_all():
    calc = StringCalculator()
    assert calc.add("1,2|3\n5") == 11

