#!/usr/bin/python3

"""
    Minimum operations project
"""


def minOperations(n):
    """
        Function of the minimum operation
        return:
               number of minimum operations
    """

    a = 1
    b = 0
    operation = 0
    while a < n:
        left_over = n - a
        if (left_over % a == 0):
            b = a
            a += b
            operation += 2
        else:
            a += b
            operation += 1
    return operation
