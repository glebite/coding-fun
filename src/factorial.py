"""
factorial.py


From Wikipedia:

In mathematics, the factorial of a positive integer n,
denoted by n!, is the product of all positive integers
less than or equal to n:

{\displaystyle n!=n\times (n-1)\times (n-2)\times (n-3)
\times \cdots \times 3\times 2\times 1\,.}{\displaystyle 
n!=n\times (n-1)\times (n-2)\times (n-3)\times
\cdots \times 3\times 2\times 1\,.}
For example,

{\displaystyle 5!=5\times 4\times 3\times 2\times 1=120\,.}{\displaystyle 5!=5\times 4\times 3\times 2\times 1=120\,.}
The value of 0! is 1, according to the convention for an empty product.

It is often made into a recursive formula as follows:

factorial N:
    if N is 0,
        return 1 (factorial of 0 = 1)
    return N * factorial of N -1
"""


def factorial(n):
    """
    factorial docstring - more details in file header
    """
    if not isinstance(n, int) or isinstance(n, bool):
        # booleans act like ints
        raise TypeError
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))
