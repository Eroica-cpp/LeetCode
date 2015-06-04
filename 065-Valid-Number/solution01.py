#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 065-Valid-Number
# Link:     https://leetcode.com/problems/valid-number/
# ==============================================================================
# Validate if a given string is numeric.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# 
# Note: It is intended for the problem statement to be ambiguous. You should 
# gather all requirements up front before implementing one.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your 
# function signature accepts a const char * argument, please click the reload button  to reset your code definition.
# ==============================================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: A boring and meaningless question
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.lower()
        s = s.strip()

        for i in s:
            if i not in [str(j) for j in range(0,10)]+['.','e','-','+']:
                return False
        for i in ['.','e']:
            if s.count(i) >= 2:
                return False

        for i in xrange(1,len(s)):
            if s[i] in ['-','+'] and s[i-1] != 'e':
                return False

        new = ""
        for i in s:
            if i not in ['-', '+']:
                new += i
        s = new

        if '.' not in s and 'e' not in s:
            return s != ""
        elif '.' not in s:
            a, b = s.split('e')
            return a != "" and b != ""
        elif 'e' not in s:
            a, b = s.split('.')
            return a != "" or b != ""
        else:
            i, j = s.index('.'), s.index('e')
            if i > j:
                return False
            a, b, c = s[:i], s[i+1:j], s[j+1:]
            return (a != "" or b != "") and c != ""

if __name__ == '__main__':
    s = "0" # => true
    s = " 0.1 " # => true
    s = "abc" # => false
    s = "1 a" # => false
    s ="2e10" # => true
    s = ".1" # => true
    s = "." # => false
    s = "01" # => true
    s = ".e1" # => false
    s = "01." # => true
    s = "6+1" # => false
    s = " 005047e+6" # => true
    s = "2e+60++604" # => false
    s = "256523.e02" # => true
    s = ".0e" # => false
    print Solution().isNumber(s)