"""
Create a function that returns the sum of the two lowest positive numbers given
an array (list?) of at least 4 positive integers (no floats or non-integer values will
be passed).
"""

def sumFn(list):
    smallest1 = min(list)
    list.remove(smallest1)
    smallest2 = min(list)
    return smallest1 + smallest2
