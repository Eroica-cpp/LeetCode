#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 19, 2015
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
Method: use extra space
Time Complexity: O(n)
Space Complexity: O(n)
Note: try in-place solution next round
==============================================================================
"""

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        stack = []
        size = len(s)
        i = 0
        word = ""
        while i <= size:
            if i == size or s[i] == " ":
                stack.append(word)
                word = ""
            else:
                word += s[i]
            i += 1

        new = []
        while stack:
            new += [i for i in stack.pop()] + [" "]
        s[:] = new[:-1]

if __name__ == '__main__':
    s = "the sky is blue"
    s = [i for i in s]
    Solution().reverseWords(s)
    print s