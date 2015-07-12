#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 068-Text-Justification
Link:     https://leetcode.com/problems/text-justification/
====================================================================================
Given an array of words and a length L, format the text such that each line has 
exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as 
you can in each line. Pad extra spaces ' ' when necessary so that each line has 
exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the 
number of spaces on a line do not divide evenly between words, the empty slots 
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is 
inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do 
in this case?
In this case, that line should be left-justified.
====================================================================================
Method: 
====================================================================================
"""

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        res = []
        size = len(words)
        begin = currLength = 0

        for i in xrange(size):
            if currLength + len(words[i]) + (i - begin) > maxWidth:
                res.append(self.connect(words, begin, i - 1, currLength, maxWidth, False))
                begin = i
                currLength = 0
            currLength += len(words[i])

        res.append(self.connect(words, begin, size - 1, currLength, maxWidth, True))
        return res

    def connect(self, words, begin, end, currLength, maxWidth, isLast):
        s = ""
        n = end - begin + 1
        for i in xrange(n):
            s += words[begin + i]
            s += self.addSpace(i, n - 1, maxWidth - currLength, isLast)

        if len(s) < maxWidth: s += " " * (maxWidth - len(s))
        return s

    def addSpace(self, i, n, maxWidth, isLast):
        if n < 1 or i > n - 1: return ""
        spaceNum = 1 if isLast else (maxWidth/n + int(i < (maxWidth%n)))
        return " " * spaceNum

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16
    print Solution().fullJustify(words, L)