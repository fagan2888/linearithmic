#!/usr/bin/env python

"""
Requirement:
    Create a function that takes an input that will be some multiple of 100.
    The function should return the sum of all the digits up to and including 
    that number except for any numbers with a penultimate digit of seven.

Example:
    Given an input of 100, it should add up all the numbers from 1 to 69,
    skip numbers 70 to 79 and then continue adding from 80 to 100.
    >>> no_penultimate_sevens(100)
    >>> 4305
"""

def no_penultimate_sevens_naive(n:int) -> int:
    res = 0
    for i in range(n + 1):
        s = str(i)
        if len(s) > 1 and s[-2] == '7':
            pass
        else:
            res += i
    return res

def no_penultimate_sevens_naive_list_comp(n:int) -> int:
    return sum([i for i in range(n + 1) if (i < 10 or str(i)[-2] != '7')])

HUNDRED_BASE = 100
THOUSANDS_BASE = 1000
EXCLUSION_BASE = 70
EXCLUSION_MAX = 79

def no_penultimate_sevens_constant(n:int) -> int:

    # n must be a multiple of 100
    assert(n % HUNDRED_BASE == 0)

    # define the sequence sum function with optional start parameter
    seq_sum = lambda n,start=0: n * (n + 1) // 2 if start == 0 else seq_sum(n) - seq_sum(start - 1)

    # a more generalized implmentation is below, but will need to explain it later
    #seq_sum = lambda n,start=0,difference=1: ((n+1) // 2) * (2*start + (n)*difference)

    # get the total sum from 0 to n
    all_nums_total = seq_sum(n)

    # get the number of hundreds that will occur with penunltimate digit 7
    hundreds_total = THOUSANDS_BASE * seq_sum(n // HUNDRED_BASE - 1) 

    # get the sum of all the 70s values that will be excluded 
    seventies_total = seq_sum(EXCLUSION_MAX,EXCLUSION_BASE) * (n // HUNDRED_BASE)

    # return the total minus exclusions
    return all_nums_total - hundreds_total - seventies_total

for i in range(1,100):
    assert(no_penultimate_sevens_naive(i * HUNDRED_BASE) == no_penultimate_sevens_naive_list_comp(i * HUNDRED_BASE))
    assert(no_penultimate_sevens_naive(i * HUNDRED_BASE) == no_penultimate_sevens_constant(i * HUNDRED_BASE))

print("ALL CHECKS PASSED")
