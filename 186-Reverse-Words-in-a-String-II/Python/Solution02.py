#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 3, 2015
Question: 186-Reverse-Words-in-a-String-II
Link:     https://leetcode.com/problems/reverse-words-in-a-string-ii/
==============================================================================
Given an input string, reverse the string word by word. A word is defined as 
a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words 
are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
==============================================================================
Method: reverse in place; first reverse the whole string, then reverse single word
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        size = len(s)
        for i in xrange(size/2):
            s[i], s[-i-1] = s[-i-1], s[i]

        begin = end = 0
        for i in xrange(size+1):
            if i == size or s[i] == " ":
                end = i
                self.reverse(s, begin, end)
                begin = end + 1

    def reverse(self, s, begin, end):
        for i in xrange((end - begin) / 2):
            s[begin + i], s[end - i - 1] = s[end - i - 1], s[begin + i]

if __name__ == '__main__':
    s = "the sky is blue"
    s = [i for i in s]
    Solution().reverseWords(s)
    print s
