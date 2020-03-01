from src.factorial import factorial


def test_check_one():
    x = factorial(1)
    assert x == 1

def test_check_two():
    x = factorial(2)
    assert x == 2

def test_check_three():
    x = factorial(3)
    assert x == 6

def test_check_five():
    x = factorial(5)
    assert x == 120

def test_check_string():
    try:
        x = factorial('x')
        assert Fail
    except TypeError as exception_out:
        assert True
