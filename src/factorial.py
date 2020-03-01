"""
factorial.py



"""

def factorial(n):
    """
    factorial docstring
    """
    if not isinstance(n, int) or isinstance(n, bool):
        # booleans act like ints
        raise TypeError
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

