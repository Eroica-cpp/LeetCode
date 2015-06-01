#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 11, 2015
# Question: 017-Letter-Combinations-of-a-Phone-Number
# Link:     https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# ==============================================================================
# Given a digit string, return all possible letter combinations that the 
# number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is 
# given below.
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# Note:
# Although the above answer is in lexicographical order, your answer could 
# be in any order you want.
# ==============================================================================
# Method: Recursion
# Time Complexity: Exp
# Space Complexity: Exp
# ==============================================================================

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        numberMap = [" ","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        if not digits:
            return []
        elif len(digits) == 1:
            return [i for i in numberMap[int(digits[0])]]

        res = []
        for i in numberMap[int(digits[0])]:
            for j in self.letterCombinations(digits[1:]):
                res.append(i+j)

        return res

if __name__ == '__main__':
    digits = "234"
    print Solution().letterCombinations(digits)