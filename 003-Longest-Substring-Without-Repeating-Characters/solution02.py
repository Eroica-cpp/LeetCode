#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 11, 2015
# Question: 003-Longest-Substring-Without-Repeating-Characters
# Link:     https://leetcode.com/problems/longest-substring-without-repeating-characters/
# ==============================================================================
# Given a string, find the length of the longest substring without repeating 
# characters. For example, the longest substring without repeating letters for 
# "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring 
# is "b", with the length of 1.
# ==============================================================================
# Method: Hash Table
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Note: Still "Time Limit Exceeded"
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        maxVal = 0
        counter = 0
        while counter <= len(s) - 1:
            new = {}
            for i in s[counter:]:
                if new.get(i):
                    break
                else:
                    new[i] = 0
            counter += 1
            maxVal = max(maxVal, len(new))

        return maxVal

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("cbaa21345678sfddsfsdf")