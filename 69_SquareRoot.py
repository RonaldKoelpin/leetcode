#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.



Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

    0 <= x <= 231 - 1

"""

# linear search
def mySqrt(x: int) -> int:
    for i in range(x+2):
        if i*i > x:
            return i-1

# bisection search
def mySqrt2(x: int) -> int:
    # base cases
    if x == 0: return 0
    if x == 1: return 1
    # range of possible sqrts
    lower, upper = 1, x
    ans = 0
    # binary searching for sqrt
    while lower <= upper:
        mid = int((lower+upper)/2)
        square = mid*mid
        if square == x:
            return mid
        elif square < x:
            ans = mid
            lower = mid + 1
        else: # square > x
            upper = mid - 1
    return ans

if __name__ == "__main__":
    x = 2**(31)-1
    print(mySqrt2(x))
