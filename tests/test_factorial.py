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
        assert False
    except TypeError as exception_out:
        assert True

def test_check_boolean():
    try:
        x = factorial(True)
        assert False
    except TypeError as exception_out:
        assert True

def test_check_float():
    try:
        x = factorial(3.141)
        assert False
    except TypeError as exception_out:
        assert True

def test_check_list():
    try:
        x = factorial([1,2,3,34])
        assert False
    except TypeError as exception_out:
        assert True        

def test_check_dict():
    try:
        x = factorial({'a': 3, 'b': 4})
        assert False
    except TypeError as exception_out:
        assert True        
        
