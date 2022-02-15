"""Generalization"""
from locale import currency


def fib(n):
    """Compute the nth Fibonacci number?, for N >= 1."""
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence
    
    >>> summation(5, cube)
    225
    """
    total, k =0, 1
    while k <=n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first N natural number
    
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)