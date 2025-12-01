#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ugly.py
first version: 2025-11-24
this version 2025-11-24
@author: rk

An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.


Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.

Example 3:


Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.


Constraints:

    -2^31 <= n <= 2^31 - 1
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        prime_factors = []
        ugly = [2,3,5]
        nice = []

        for i in range(2,n+1,1):
            while (n%i)==0 and n > 0:
                prime_factors.append(i)
                n = int(n/i)

        for prime in prime_factors:
            if prime not in ugly:
                nice.append(prime)

        # print(prime_factors)
        # print(nice)
        return(len(nice)==0)

class Solution2:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        ugly = [2,3,5]
        for num in ugly:
            while (n%num)==0 and n > 0:
                n = n/num

        return(n==1)

sol = Solution()
print(sol.isUgly(32742))
