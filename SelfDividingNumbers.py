#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q3. Self Dividing Numbers
Easy

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).



Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]



Constraints:

    1 <= left <= right <= 10^4

"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> [int]:
        all_numbers = range(left, right+1, 1)
        self_dividing_numbers = []

        for number in all_numbers:
            s = str(number)
            self_dividing = True
            for i in range(len(s)):
                n = int(s[i])
                if n == 0:
                    self_dividing = False
                    break
                elif number%n != 0:
                    self_dividing = False
                    break
            if self_dividing:
                self_dividing_numbers.append(number)

        return self_dividing_numbers

class Solution2:
    def selfDividingNumbers(self, left: int, right: int) -> [int]:
        all_numbers = range(left, right+1, 1)
        self_dividing_numbers = []

        for number in all_numbers:
            num = number
            self_dividing = True
            while num > 0:
                rem = num%10
                if rem == 0:
                    self_dividing = False
                    break
                elif number%rem != 0:
                    self_dividing = False
                    break
                num = int((num-rem)/10)
            if self_dividing:
                self_dividing_numbers.append(number)

        return self_dividing_numbers

if __name__ == '__main__':
    left, right = 47, 85
    print(f"Left = {left}, Right = {right}")
    print("Solution 1")
    sol = Solution()
    sdn = sol.selfDividingNumbers(left, right)
    print(sdn)
    print("Solution 2")
    sol2 = Solution2()
    sdn = sol2.selfDividingNumbers(left, right)
    print(sdn)
