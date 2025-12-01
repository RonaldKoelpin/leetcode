#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q1. Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"

Example 3:

Input: n = 3, k = 1
Output: "123"

Constraints:

    1 <= n <= 9
    1 <= k <= n!

"""
import math

class Solution:
    def Permutations(self, set) -> list:
        n = len(set)
        if n == 0:
            # print(f"n = {n}. Returning empty set.")
            return []
        elif n == 1:
            # print(f"n = {n}. Returning identity permutation.")
            return [set]
        # set = [i for i in range(1, n+1, 1)]
        # print(f"n = {n}. Setting up recursion.")
        permutations = []
        for i in range(n):
            elem = set[i]
            rem = set[:i] + set[i+1:]
            # print(f"Choosen element: {elem}.")
            # print(f"Remainder: {rem}")
            for perm in self.Permutations(rem):
                # print(perm)
                permutations.append([elem] + perm)
        return permutations

    def getPermutation(self, n: int, k: int) -> str:
        permuation = self.Permutations(list(range(1,n+1,1)))[k-1]
        string = ""
        while permuation:
            string = string + str(permuation.pop(0))
        return string

class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1,n+1,1))
        res = ""
        while numbers:
            num_blocks = n
            num_elements_per_block = math.factorial(n-1)
            # print(f"{n} blocks, {num_elements_per_block} elements per block")
            num_block = int(k/num_elements_per_block)
            k = k % num_elements_per_block
            if k == 0:
                num_block = num_block - 1
                k = k + num_elements_per_block
            # print(f"Looking for element #{k} in Block num {num_block}")
            res = res + str(numbers.pop(num_block))
            # print(res)
            n = n - 1
        return res

if __name__ == "__main__":
    n = 9
    k = 91720
    set = list(range(1,n+1,1))
    sol = Solution()
    sol2 = Solution2()
    # print(sol.Permutations(set))
    print(sol.getPermutation(n, k))
    print(sol2.getPermutation(n, k))


