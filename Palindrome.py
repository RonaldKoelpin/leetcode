#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palindrome.py
first version: 2025-11-24
this version 2025-11-24
@author: rk

Given an integer x, return true if x is a Palindrome (reads the same forwards and backwards), and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""

# my solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(int(n/2)):
            if s[i] != s[n-1-i]:
                return False
        return True

    def isPalindromeNoString(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        while x > 0:
            rem = x%10
            digits.append(rem)
            x = int((x-rem)/10)
        n = len(digits)
        for i in range(int(n/2)):
            if digits[i] != digits[n-1-i]:
                return False
        return True

if __name__ == "__main__":
    x = 2**17
    sol = Solution()
    print(f"Checking x = {x}:")
    print(sol.isPalindrome(x))
    print(sol.isPalindromeNoString(x))