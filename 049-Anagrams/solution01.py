#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 3, 2015
# Question: 049-Anagrams
# Link:     https://leetcode.com/problems/anagrams/
# ==============================================================================
# Given an array of strings, return all groups of strings that are anagrams.
# 
# Note: All inputs will be in lower-case.
# ==============================================================================
# Method: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: the problem definition is confusing!
# ==============================================================================

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dic = {}
        for s in strs:
            key = "".join(sorted([i for i in s]))
            dic[key] = dic.get(key)+[s] if dic.get(key) else [s]

        res = []
        for val in dic.values():
            if len(val) >= 2:
                res += val

        return res

if __name__ == '__main__':
    strs = []
    strs = ["tea","and","ate","eat","den"] # expected: ["tea","ate","eat"]
    strs = ["tea","and","ate","eat","dan"] # expected: ["and","dan","tea","ate","eat"] this one and above is different !
    # strs = [""] # expected: []
    # strs = ["", ""] # expected: ["",""]
    # strs = ["a"] # expected: []
    # strs = ["","b"] # expected: []
    # strs = ["tea","","eat","","tea",""] # expected: ["","","","tea","eat","tea"]
    print Solution().anagrams(strs)