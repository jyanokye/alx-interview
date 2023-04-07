#!/usr/bin/python3
"""Minimum operations"""

def min_operations(n):
    """
       function for the minimum
       operation
       return:
              minimum number of operations
    """ 
    if n < 2:
        return 0

    operations, factor = 0, 2

    while factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
            factor -= 1

        factor += 1

    return operations
