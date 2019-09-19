'''
Write a function that takes a positive three-digit number as input and returns the sum of its digits.

The function should have a name digit_sum and take an argument n.
'''

def digit_sum(n):
    return n // 100 + n // 10 % 10 + n % 10
