#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 11, 2015
Question: 254-Factor-Combinations
Link:     https://leetcode.com/problems/factor-combinations/
==============================================================================
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations 
of its factors.

Note: 
Each combination's factors must be sorted ascending, for example: The factors 
of 2 and 6 is [2, 6], not [6, 2].

You may assume that n is always positive.
Factors should be greater than 1 and less than n.

Examples: 

input: 1
output: []

input: 37
output: []

input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
==============================================================================
Method: recursion
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        res = []

        for i in xrange(2, int(n**0.5 + 1)):
            if n % i == 0: 
                res += [[i, n/i]] + [[i] + _ for _ in self.getFactors(n / i) if _ and _[0] >= i]

        return res

if __name__ == '__main__':
    n = 12
    print Solution().getFactors(n)