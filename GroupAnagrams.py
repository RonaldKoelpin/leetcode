#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]


Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""
from collections import defaultdict # easier handling of previously non existent keys

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list) # values in our dict are lists; keys are sorted strings (TUPLES!)
    ans = []
    for string in strs:
        sorted_string = tuple(sorted(string)) # sorting a string returns a list which is mutable and therefore not hashable
        anagrams[sorted_string].append(string)

    return list(anagrams.values())

def main():
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = [""]
    strs3 = ["a"]
    print(groupAnagrams(strs1))
    print(groupAnagrams(strs2))
    print(groupAnagrams(strs3))

if __name__ == "__main__":
    main()