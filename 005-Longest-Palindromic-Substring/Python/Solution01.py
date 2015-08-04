#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 1, 2015
# Question: 005-Longest-Palindromic-Substring
# Link:     https://leetcode.com/problems/longest-palindromic-substring/
# ==============================================================================
# Given a string S, find the longest palindromic substring in S. You may 
# assume that the maximum length of S is 1000, and there exists one unique 
# longest palindromic substring.
# ==============================================================================
# Method: Expand around center; handle one center and two centers cases separately
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Note: 
# 1. Reference http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-i.html
# 2. Try O(n) method: http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        maxVal = 0
        size = len(s)
        res = ""

        if size <= 1:
            return s
        elif size == 2:
            return s if s[0] == s[1] else s[0]

        # one center
        for i in xrange(size):
            left, right = i-1, i+1
            while left >= 0 and right < size:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            
            if right-left-2 > maxVal:
                maxVal = right-left-2
                res = s[left+1:right]

        # two centers
        for i in xrange(size-1):
            left, right = i-1, i+2
            if s[i] != s[i+1]:
                continue
            
            while left >= 0 and right < size:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            
            if right-left-2 > maxVal:
                maxVal = right-left-2
                res = s[left+1:right]

        return res

if __name__ == '__main__':
    s = "1233321"
    print Solution().longestPalindrome(s)

