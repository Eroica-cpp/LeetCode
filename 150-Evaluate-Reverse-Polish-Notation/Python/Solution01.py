#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 10, 2015
Question: 150-Evaluate-Reverse-Polish-Notation
Link:     https://leetcode.com/problems/evaluate-reverse-polish-notation/
==============================================================================
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
==============================================================================
Method: use a stack
Time Complexity: O(n)
Space Complexity: O(log n)
Note: 
1. "6 / -132 -> -1" in python, while the answer is 0 in C++
2. use "int(float(x)/y)" to avoid this trick
==============================================================================
"""

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i in operators:
                y = stack.pop()
                x = stack.pop()
                if i == "+": x += y
                elif i == "-": x -= y
                elif i == "*": x *= y
                elif i == "/": x = int(float(x)/y)
                stack.append(x)
            else:
                stack.append(int(i))
                
        return stack[-1]
