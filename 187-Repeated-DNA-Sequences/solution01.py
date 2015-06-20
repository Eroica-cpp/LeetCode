#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 20, 2015
Question: 187-Repeated-DNA-Sequences
Link:     https://leetcode.com/problems/repeated-dna-sequences/
==============================================================================
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to 
identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that 
occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
==============================================================================
Method: Hash Table
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        size = len(s)
        if size < 10:
            return []
        
        dic = {}
        for i in xrange(size-9):
            dic[s[i:i+10]] = dic.get(s[i:i+10])+1 if dic.has_key(s[i:i+10]) else 1

        return [key for key,val in dic.items() if val >= 2]

if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    s = "AAAAAAAAAAAAA"
    print Solution().findRepeatedDnaSequences(s)