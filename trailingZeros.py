#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0

Constraints:

    0 <= n <= 104

Follow up: Could you write a solution that works in logarithmic time complexity?

"""
import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # DOESNT WORK FOR LARGE NUMBERS
        res = math.factorial(n)
        print(f"{n}! = {res}")
        digits = []
        # extracting all digits
        while res > 0:
            rem = res%10
            print(f"{res} mod 10 = {rem}.")
            digits.append(rem)
            print(digits)
            res = int((res-rem)/10)
            print(f"New number = {res}")
        print(f"Digits = {digits}")
        # checking for zeros
        num_zeros = 0
        for i in range(len(digits)):
            print(f"Current Digit = {digits[i]}")
            if digits[i] == 0: num_zeros += 1
            else: return num_zeros
        return num_zeros

    def trailingZeroes2(self, n: int) -> int:
        num_twos = 0
        num_fives = 0
        for i in range(2,n+1,1):
            num = i
            # print(f"Current factor = {num}")
            while num > 0:
                if num%2 == 0:
                    # print("is divisble by 2")
                    num_twos += 1
                    num = int(num/2)
                elif num%5 == 0:
                    # print("is divisible by 5")
                    num_fives += 1
                    num = int(num/5)
                else: break
            # print(f"Number of 2s in product = {num_twos}")
            # print(f"Number of 5s in product = {num_fives}")

        return min(num_twos, num_fives)

    def trailingZeroes3(self, n: int) -> int:
        count = 0
        divisor = 5
        while n >= divisor:
            count = count + int(n/divisor)
            divisor = divisor * 5
        return count

if __name__ == "__main__":
    n = 100
    sol = Solution()
    print(sol.trailingZeroes2(n))
    print(sol.trailingZeroes3(n))
    print(f"{n}! = {math.factorial(n)}")