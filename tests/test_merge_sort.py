"""
test_merge_sort.py - includes tests for the homogenous check code
"""
from src.merge_sort import * 


def test_check_even_size():
    test_data = [5,7,8,1,2,3]
    merge(test_data)
    assert test_data == [1,2,3,5,7,8]

def test_check_odd_size():
    test_data = [13,5,7,8,1,2,3]
    merge(test_data)
    assert test_data == [1,2,3,5,7,8,13]

def test_check_empty():
    test_data = []
    merge(test_data)
    assert test_data == []

def test_check_strings():
    test_data = ['Mana', 'Paul', 'Johanna', 'Robert', 'Mike']
    merge(test_data)
    assert test_data == ['Johanna', 'Mana', 'Mike', 'Paul', 'Robert']

def test_check_bools():
    test_data = [True, False, False, True, False]
    merge(test_data)
    assert test_data == [False, False, False, True, True]

def test_check_floats():
    test_data = [3.5, 2.7, 3.141, 0.0, 2.141]
    merge(test_data)
    assert test_data == [0.0, 2.141, 2.7, 3.141, 3.5]

def test_check_sorted():
    test_data = [1,2,3,4,5,6,7,8]
    merge(test_data)
    assert test_data == [1,2,3,4,5,6,7,8]

def test_check_negative_ints():
    test_data = [8,7,6,-1,-13]
    merge(test_data)
    assert test_data == [-13, -1, 6, 7, 8]

def test_homogenous():
    check = homogenous_type([1,2,3,4])
    assert check is True

def test_homogenous_not():
    check = homogenous_type([1,'a', 3.5])
    assert check is False
