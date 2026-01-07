#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
50. Pow(x, n)
Medium
Topics
premium lock iconCompanies

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

    -100.0 < x < 100.0
    -231 <= n <= 231-1
    n is an integer.
    Either x is not zero or n > 0.
    -104 <= xn <= 104

"""

def myPow(x: float, n: int) -> float:
    if x == 0 and n <= 0:
        return None
    elif x == 0:
        return 0
    elif x == 1:
        return 1
    elif n == 0:
        return 1
    ans = 1
    if n > 0:
        for i in range(n):
            ans = ans * x
    else: # n < 0
        for i in range(-n):
            ans = ans/x
    return ans

def myPow2(x: float, n: int) -> float:
    if x == 0 and n <= 0: return None
    elif x == 0: return 0
    elif x == 1: return 1
    elif n == 0: return 1
    ans = 1
    if n < 0:
        n = -n
        x = 1/x
    while n:
        if n%2 == 1:
            ans = ans * x
        x = x * x
        n = n//2
    return ans

if __name__ == "__main__":
    x, n = 2, 5
    print(myPow(x,n))
    print(myPow2(x,n))
