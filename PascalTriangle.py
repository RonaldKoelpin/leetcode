#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

    1 <= numRows <= 30

"""
import math

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for row in range (numRows):
            coeffs = []
            for pos in range(row+1):
                coeffs.append(math.comb(row, pos))
            res.append(coeffs)
        return res

    def generateTriangle(self, numRows: int) -> list[list[int]]:
        res = []
        for row in range(numRows):
            coeffs = []
            for pos in range(row+1):
                if pos == 0 or pos == row:
                    coeffs.append(1)
                else:
                    coeff = res[row-1][pos-1] + res[row-1][pos]
                    coeffs.append(coeff)
            res.append(coeffs)
        return res

if __name__ == "__main__":
    numRows = 10
    sol = Solution()
    print(sol.generate(numRows))
    print(sol.generateTriangle(numRows))
