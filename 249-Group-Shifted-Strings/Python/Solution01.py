#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 8, 2015
Question: 249-Group-Shifted-Strings
Link:     https://leetcode.com/problems/group-shifted-strings/
==============================================================================
Given a string, we can "shift" each of its letter to its successive letter, 
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings 
that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the 
lexicographic order.
==============================================================================
Method: hash table; use difference of ascii code of each character in the string as key
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        dic = {}
        for s in strings:
            code = self.getCode(s)
            if dic.has_key(code): dic[code].append(s)
            else: dic[code] = [s]

        return [sorted(i) for i in dic.values()]

    def getCode(self, s):
        code = ""
        for i in xrange(len(s)):
            code += "|" + str((ord(s[i]) - ord(s[i-1])) % 26)
        return code

if __name__ == '__main__':
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print Solution().groupStrings(strings)