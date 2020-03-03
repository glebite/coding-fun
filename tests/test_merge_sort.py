from src.merge_sort import merge


def test_check_even_size():
    test_data = [5,7,8,1,2,3]
    merge(test_data)
    assert test_data == [1,2,3,5,7,8]

def test_check_odd_size():
    test_data = [13,5,7,8,1,2,3]
    merge(test_data)
    assert test_data == [1,2,3,5,7,8,13]
