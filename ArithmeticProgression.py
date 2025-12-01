#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ArithmeticProgression.py
first version: 2025-11-23
this version 2025-11-23
@author: rk

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.



Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:

    2 <= arr.length <= 1000
    -106 <= arr[i] <= 106
"""

# my solution
class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr.sort()
        length = len(arr)
        increment = arr[1] - arr[0]
        for i in range(length-1):
            diff = arr[i+1]-arr[i]
            if(diff != increment):
                return(False)
        return(True)

# faster Solution
class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr.sort()
        s = set()
        for i in range(len(arr)-1):
            s.add(arr[i+1]-arr[i])
        return len(s) == 1
