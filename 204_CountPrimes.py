#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q1. Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.


Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0



Constraints:

    0 <= n <= 5 * 106

"""

# solution 1: works but slow due to list comprehension
def countPrimes(n: int) -> int:
    if n <= 2: return 0
    num_primes = 0
    all_numbers = list(range(2, n, 1))
    while all_numbers:
        current = all_numbers.pop(0)  # take out smallest number left
        num_primes += 1  # increase prime count by 1
        # take out all multiples of current number
        k = 2
        while k * current <= n:
            if k * current in all_numbers:
                all_numbers.remove(k * current)
            k += 1
    return num_primes

# solution 2
def count_primes(n: int) -> int:
    if n <= 2: return 0
    is_prime = [True] * n # initialize all numbers as prime
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p: n: p] = [False] * len(range(p * p, n, p))
    return sum(is_prime)
    # extracting the actual prime numbers

# actually listing all primes < n
def get_primes(n: int) -> [int]:
    if n <= 2: return 0
    is_prime = [True] * n # initialize all numbers as prime
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p: n: p] = [False] * len(range(p * p, n, p))
    return [i for i, val in enumerate(is_prime) if val]

def prime_generator(n: int):
    if n <= 2: return None
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p: n: p] = [False] * len(range(p * p, n, n))
    for i in range(n):
        if is_prime[i]:
            yield i

if __name__ == '__main__':
    n = 100
    print(count_primes(n))
    print(get_primes(n))