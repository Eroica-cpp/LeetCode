#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 19, 2015
Question: 159-Longest-Substring-with-At-Most-Two-Distinct-Characters
Link:     https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
==============================================================================
Given a string, find the length of the longest substring T that contains at 
most 2 distinct characters.

For example, Given s = "eceba",

T is "ece" which its length is 3.
==============================================================================
Method: one pass; two pointers; use hashtable to record repeated times
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        size = len(s)
        maxVal = begin = end = 0
        dic = {}

        while end < size:
            dic[s[end]] = dic[s[end]]+1 if dic.has_key(s[end]) else 1

            if len(dic.keys()) > 2:
                x, y = list(set(dic.keys()) - {s[end]})
                while dic[x] > 0 and dic[y] > 0:
                    if s[begin] == x: dic[x] -= 1
                    else: dic[y] -= 1
                    begin += 1

                if dic[x] == 0: dic.pop(x)
                else: dic.pop(y)

            maxVal = max(maxVal, end-begin+1)
            end += 1

        return maxVal

if __name__ == '__main__':
    s = "aaaaabbca"
    print Solution().lengthOfLongestSubstringTwoDistinct(s)