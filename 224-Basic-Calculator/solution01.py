#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 224-Basic-Calculator
# Link:     https://leetcode.com/problems/basic-calculator/
# ==============================================================================
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus 
# + or minus sign -, non-negative integers and empty spaces .
# 
# You may assume that the given expression is always valid.
# 
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# 
# Note: Do not use the eval built-in library function.
# ==============================================================================
# Method: Naive method, use a stack to record sign of every level of parentheses pairs
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        total = 0
        lst = ["+"]
        size = len(s)
        i = 0
        while i < size:
            if s[i] in "+-()":
                lst.append(s[i])
                i += 1
            elif s[i].isdigit():
                num = ""
                while i < size and s[i].isdigit():
                    num += s[i]
                    i += 1
                lst.append(num)
            else:
                i += 1

        sign_stack = [1]
        for i in xrange(len(lst)):
            if lst[i] not in "()+-":
                if i-1 < 0 or lst[i-1] == "(" or lst[i-1] == "+":
                    total += int(lst[i]) * sign_stack[-1]
                elif lst[i-1] == "-":
                    total -= int(lst[i]) * sign_stack[-1]
            elif lst[i] == "(":
                sign = sign_stack[-1] if i-1 < 0 or lst[i-1] == "+" else -sign_stack[-1]
                sign_stack.append(sign)
            elif lst[i] == ")":
                sign_stack.pop()

        return total

if __name__ == '__main__':
    s = "1 + 1"
    s = " 2-1 + 2 "
    s = "(1+(4+5+2)-3)+(6+8)"
    s = "2-(5-6)"
    s = "(5-(1+(5)))"
    print Solution().calculate(s)