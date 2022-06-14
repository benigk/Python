"""Environments for Higher-Order Functions"""
def apply_twice(f,x):
    return f(f(x))

def square(x):
    return  x * x

"""Higher-Order Function Example: Repeat"""
def repeat(f,x):
    """
    >>> repeat(g,5)
    2
    """
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y+5) // 3

"""Environments for Nested Definitions"""
def make_adder(n):
    """
    >>> make_adder(3)(8)
    11
    """
    def adder(k):
        return k + n
    return adder


def triple(x):
    return 3 * x

def compose1(f,g):
    """
    >>> compose1(square, make_adder(2))(3)
    25
    """
    def h(x):
        return f(g(x))
    return h

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

# 123123


